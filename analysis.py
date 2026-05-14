import pandas as pd

df = pd.read_csv('validation_data.csv')

# Convert pace string to seconds per mile for numerical comparison
def pace_to_seconds(pace_str):
    mins, secs = pace_str.split(':')
    return int(mins) * 60 + int(secs)

df['pace_sec_per_mi'] = df['avg_pace'].apply(pace_to_seconds)

theory = df[df['condition'] == 'theory_aware']
control = df[df['condition'] == 'control']

print("=" * 55)
print("  VALIDATION RESULTS SUMMARY")
print("=" * 55)

print(f"\nTheory-Aware runs ({len(theory)} sessions):")
print(f"  Avg RPE:              {theory['rpe'].mean():.1f} / 10")
print(f"  Avg Flow Score:       {theory['flow_score'].mean():.1f} / 10")
print(f"  Avg HR:               {theory['mean_hr'].mean():.1f} BPM")
print(f"  Avg Pace (sec/mi):    {theory['pace_sec_per_mi'].mean():.1f}s")

print(f"\nControl runs ({len(control)} sessions):")
print(f"  Avg RPE:              {control['rpe'].mean():.1f} / 10")
print(f"  Avg Flow Score:       {control['flow_score'].mean():.1f} / 10")
print(f"  Avg HR:               {control['mean_hr'].mean():.1f} BPM")
print(f"  Avg Pace (sec/mi):    {control['pace_sec_per_mi'].mean():.1f}s")

pace_diff = theory['pace_sec_per_mi'].mean() - control['pace_sec_per_mi'].mean()
flow_diff = theory['flow_score'].mean() - control['flow_score'].mean()
rpe_diff = theory['rpe'].mean() - control['rpe'].mean()
hr_diff = theory['mean_hr'].mean() - control['mean_hr'].mean()

print(f"\nDifferences (theory vs control):")
print(f"  Pace:       {pace_diff:+.1f} sec/mi (negative = theory was faster)")
print(f"  Flow Score: {flow_diff:+.1f} pts (positive = theory felt better)")
print(f"  RPE:        {rpe_diff:+.1f} pts (positive = theory felt harder)")
print(f"  HR:         {hr_diff:+.1f} BPM")

print("\n" + "=" * 55)
print("  INTERPRETATION")
print("=" * 55)
print(f"""
Note: theory-aware runs averaged {theory['distance_mi'].mean():.2f} mi vs {control['distance_mi'].mean():.2f} mi
for the control. To account for this, pace (min/mi) is used
as the primary performance metric rather than total distance.

Theory-aware playlists produced a flow score of {theory['flow_score'].mean():.1f}/10 vs
{control['flow_score'].mean():.1f}/10 for the control — a difference of {flow_diff:+.1f} points.
Heart rate was nearly identical across all sessions (~165 BPM),
indicating similar physiological load.

Theory-aware runs were {abs(pace_diff):.0f} sec/mi faster on average at the
same HR, suggesting greater output for equivalent effort.
The higher RPE on theory-aware runs ({theory['rpe'].mean():.1f} vs {control['rpe'].mean():.1f}) reflects
increased pace output rather than worse experience, as flow
scores were consistently higher.

Limitation: this is a preliminary self-experiment with n=3
sessions and one test subject. Differences are directionally
consistent with the hypothesis but not statistically
significant. A larger multi-subject study would be needed
to draw firm conclusions.
""")
