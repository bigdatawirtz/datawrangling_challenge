#!/usr/bin/env python3
import argparse
import random
import sys
import pandas as pd


def random_typo(s: str) -> str:
    if not isinstance(s, str) or s == '':
        return s
    i = random.randrange(len(s))
    c = chr(random.randint(97, 122))
    return s[:i] + c + s[i+1:]


def format_number_eu(v):
    try:
        f = float(v)
        s = f"{f:,.2f}"
        s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
        return s
    except Exception:
        return v


def dirtify(df: pd.DataFrame, seed: int, missing_frac: float, dup_frac: float, outlier_frac: float) -> pd.DataFrame:
    random.seed(seed)
    df = df.copy()

    # Work with string representation but keep original for numeric checks
    cols = list(df.columns)
    n_rows = len(df)
    n_cols = len(cols)

    # Detect numeric-like columns
    numeric = []
    for c in cols:
        coercible = pd.to_numeric(df[c], errors='coerce')
        numeric.append(coercible.notna().sum() >= max(1, int(0.5 * min(50, n_rows))))

    # Missing values: set random cells to empty string
    total_cells = n_rows * n_cols
    missing_cells = int(total_cells * missing_frac)
    for _ in range(missing_cells):
        i = random.randrange(n_rows)
        j = random.randrange(n_cols)
        df.iat[i, j] = ''

    # Duplicates: append exact and partial duplicates
    n_dups = int(max(1, n_rows * dup_frac))
    if n_dups > 0:
        exacts = df.sample(n=min(n_dups, n_rows), replace=True, random_state=seed)
        df = pd.concat([df, exacts], ignore_index=True)
        # partial duplicates
        partials = exacts.copy(deep=True)
        for idx in partials.index:
            j = random.randrange(n_cols)
            col = cols[j]
            val = partials.at[idx, col]
            if numeric[j] and pd.notna(pd.to_numeric(val, errors='coerce')):
                try:
                    partials.at[idx, col] = str(float(val) + random.choice([0.0, 0.001, -0.002]))
                except Exception:
                    partials.at[idx, col] = val
            else:
                partials.at[idx, col] = random_typo(str(val))
        df = pd.concat([df, partials], ignore_index=True)

    # Outliers and format inconsistencies in numeric columns
    n_out = int(max(1, n_rows * outlier_frac))
    numeric_indices = [i for i, v in enumerate(numeric) if v]
    for _ in range(n_out):
        if not numeric_indices:
            break
        i = random.randrange(len(df))
        j = random.choice(numeric_indices)
        col = cols[j]
        choice = random.choice(['big', 'neg', 'currency', 'commas'])
        if choice == 'big':
            df.at[i, col] = str(random.choice([999999, 10_000_000, 123456789]))
        elif choice == 'neg':
            df.at[i, col] = str(random.choice([-9999, -1_000_000]))
        elif choice == 'currency':
            df.at[i, col] = f"{random.randint(1000,100000)}€"
        elif choice == 'commas':
            df.at[i, col] = format_number_eu(df.at[i, col])

    # Typographical errors and extra categories for categorical columns
    n_typo = int(max(1, n_rows * 0.03))
    for _ in range(n_typo):
        i = random.randrange(len(df))
        j = random.randrange(n_cols)
        col = cols[j]
        val = df.iat[i, j]
        if numeric[j]:
            if pd.notna(pd.to_numeric(val, errors='coerce')):
                df.iat[i, j] = f"{val} (est)"
        else:
            choice = random.choice(['typo', 'extra', 'weird'])
            if choice == 'typo':
                df.iat[i, j] = random_typo(str(val))
            elif choice == 'extra':
                df.iat[i, j] = random.choice(['N/A', 'unknown', '-', '??', 'extraneous_value'])
            else:
                df.iat[i, j] = str(val) + random.choice(['_x', '@', '0'])

    # Extra punctuation in some values
    for _ in range(int(n_rows * 0.01)):
        i = random.randrange(len(df))
        j = random.randrange(n_cols)
        col = cols[j]
        val = df.iat[i, j]
        if pd.notna(val) and not numeric[j]:
            df.iat[i, j] = str(val) + random.choice(['!', '??', '...', '€'])

    # Incorrect headers: duplicate, add spaces, blank, and shuffle
    hdr = cols.copy()
    if hdr:
        idx = random.randrange(len(hdr))
        insert_pos = random.randrange(len(hdr) + 1)
        orig_name = hdr[idx]
        placeholder = f"__EXTRA_COL_{random.getrandbits(32)}"
        # insert a uniquely named empty column into the DataFrame, then record the duplicated header label
        df.insert(insert_pos, placeholder, [''] * len(df))
        hdr.insert(insert_pos, orig_name)
        # trailing spaces
        j = random.randrange(len(hdr))
        hdr[j] = hdr[j] + random.choice([' ', '  ', ' _'])
        # blank one
        k = random.randrange(len(hdr))
        hdr[k] = ''
        # shuffle a bit
        if len(hdr) > 3:
            shuffled = hdr.copy()
            random.shuffle(shuffled)
            hdr = shuffled

    df.columns = hdr
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--missing_frac', type=float, default=0.02)
    parser.add_argument('--dup_frac', type=float, default=0.02)
    parser.add_argument('--outlier_frac', type=float, default=0.01)
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.input, dtype=str)
    except Exception as e:
        print('Error reading input:', e, file=sys.stderr)
        sys.exit(1)

    df_dirty = dirtify(df, seed=args.seed, missing_frac=args.missing_frac, dup_frac=args.dup_frac, outlier_frac=args.outlier_frac)

    # Write using cp1252 to simulate non-UTF8 default encodings
    try:
        df_dirty.to_csv(args.output, index=False, encoding='cp1252', errors='replace')
        print('Wrote', args.output)
    except Exception as e:
        print('Error writing output:', e, file=sys.stderr)


if __name__ == '__main__':
    main()
