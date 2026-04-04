from pathlib import Path

from load_data import load_raw_data
from experiment_checks import (
    flag_mismatches,
    mismatch_summary,
    duplicate_user_summary,
)
from cleaning import remove_mismatches, remove_duplicate_users
from metrics import group_conversion_rates, group_sizes


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent

    raw_data_path = project_root / "data" / "raw" / "ab_data.csv"
    processed_data_path = project_root / "data" / "processed" / "ab_clean.csv"
    summary_path = project_root / "outputs" / "tables" / "experiment_summary.csv"

    # Load raw data
    df = load_raw_data(raw_data_path)

    # Flag mismatches
    df_checked = flag_mismatches(df)

    # Summarize mismatches
    mismatch_info = mismatch_summary(df_checked)

    print("=== Mismatch Summary ===")
    print(f"Total rows: {mismatch_info['total_rows']}")
    print(f"Mismatch rows: {mismatch_info['mismatch_rows']}")
    print(f"Mismatch rate: {mismatch_info['mismatch_rate']:.6f}")

    print("\nGroup vs Landing Page:")
    print(mismatch_info["group_landing_page_table"])

    print("\nMismatch breakdown:")
    print(mismatch_info["mismatch_breakdown"])

    # Remove mismatches
    df_clean = remove_mismatches(df_checked)

    # Summarize duplicates before removing them
    duplicate_info = duplicate_user_summary(df_clean)

    print("\n=== Duplicate User Summary ===")
    print(f"Total rows: {duplicate_info['total_rows']}")
    print(f"Unique users: {duplicate_info['unique_users']}")
    print(f"Users appearing more than once: {duplicate_info['num_duplicate_users']}")
    print(f"Extra duplicate rows: {duplicate_info['extra_duplicate_rows']}")

    # Remove duplicate users
    df_clean = remove_duplicate_users(df_clean)

    print("\n=== Final Cleaned Dataset ===")
    print(f"Rows after cleaning: {len(df_clean)}")
    print(f"Unique users after cleaning: {df_clean['user_id'].nunique()}")

    # Save cleaned dataset
    processed_data_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(processed_data_path, index=False)

    print(f"\nCleaned dataset saved to: {processed_data_path}")

    # Compute summary metrics
    conversion_rates = group_conversion_rates(df_clean)
    group_counts = group_sizes(df_clean)

    summary_df = (
        conversion_rates.rename("conversion_rate")
        .to_frame()
        .join(group_counts.rename("n_users"))
    )

    # Save summary table
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path)

    print(f"Summary table saved to: {summary_path}")


if __name__ == "__main__":
    main()