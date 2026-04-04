# Project Structure

## Module Overview

### `src/load_data.py`
- `load_raw_data(path)`  
Loads the raw experiment dataset.

### `src/experiment_checks.py`
- `flag_mismatches(df)`  
Flags rows where assigned group and landing page do not match.

- `mismatch_summary(df)`  
Summarizes contamination caused by group-page mismatches.

- `duplicate_user_summary(df)`  
Summarizes duplicate user records.

### `src/cleaning.py`
- `remove_mismatches(df)`  
Removes contaminated rows with mismatched group-page assignments.

- `remove_duplicate_users(df)`  
Keeps one valid observation per user.

### `src/metrics.py`
- `group_conversion_rates(df)`  
Computes conversion rates for control and treatment groups.

- `group_sizes(df)`  
Returns sample sizes by group.

- `observed_difference(df)`  
Computes the observed conversion difference between treatment and control.

### `src/inference.py`
- `run_proportion_test(df)`  
Runs the statistical test comparing treatment vs control conversion.

- `confidence_interval_diff(df)`  
Computes the confidence interval for the conversion rate difference.

- `compute_mde(control_rate, n_per_group, alpha=0.05, power=0.80)`  
Estimates the minimum detectable effect for the experiment.

### `src/decision.py`
- `practical_threshold(control_rate, relative_lift=0.01)`  
Defines the minimum business-relevant uplift threshold.

- `business_summary(...)`  
Summarizes whether the observed result is statistically and practically meaningful.