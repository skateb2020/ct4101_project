# Basketball Movement Efficiency Prediction using Player Biomechanics
## Dataset: Basketball Movement Biomechanics Dataset
  - **Source:** Kaggle (uploaded by Zayn1999)
  - **License:** CC0: Public Domain
  - **Citation:** Zayn1999. (2026, July). Basketball Movement Biomechanics Dataset:
Biomechanical Data for Basketball Performance, Version 1. Retrieved 28 September
2026 from [https://www.kaggle.com/datasets/zayn1999/basketball-movement-biomechanics-dataset](https://www.kaggle.com/datasets/zayn1999/basketball-movement-biomechanics-dataset).

## Model Goal
  - **Regression Question:** Given a player's joint angles, velocities, and stability metrics, what is
the athlete’s movement efficiency score while playing basketball?
  - **Input Features:** movement_type, hip_flexion_angle_deg, hip_abduction_angle_deg,
knee_flexion_angle_deg, ankle_flexion_angle_deg, shoulder_flexion_angle_deg,
shoulder_abduction_angle_deg, elbow_flexion_angle_deg, wrist_flexion_angle_deg,
trunk_flexion_angle_deg, hip_angular_velocity_deg_s, knee_angular_velocity_deg_s,
ankle_angular_velocity_deg_s, shoulder_angular_acceleration_deg_s2,
elbow_angular_acceleration_deg_s2, wrist_angular_acceleration_deg_s2,
center_of_mass_velocity_m_s, vertical_jump_height_cm, ground_contact_time_ms,
movement_duration_ms, balance_score, movement_stability_score,
movement_symmetry_pct
  - **Target Variable** movement_efficiency_score

## Environment Setup and Run Instructions
To run this project locally, follow the steps below:
### Prerequisites:
**Python**: 3.12 (compatible with 3.10+) <br>
**Git**: installed and configured
### Step 1: Clone repository
```
git clone git@github.com:skateb2020/ct4101_project.git
cd ct4101_project
```
### Step 2: Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
### Step 3: Install dependencies from requirements.txt
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Step 4: Run workflow
```
jupyter lab
```
