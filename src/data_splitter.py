'''
Reusable Python script for loading and splitting the data
- dataset must be split in the same way for each model to ensure fairness during comparison
- instead of copying the same code into every model notebook, I decided to move the loading and splitting code into a separate Python script

Explanation of Splitting Design
- could not use Random Split because having a sample of the same player in training and testing would cause data leakage as the model could infer from this player that it has been trained on
- used GroupShuffleSplit and grouped by player_id to group by players and prevent data leakage
- split data into training - 70%, validation - 15%, testing - 15% from the guidelines from lecture (training - 65-80%, validation - 10-20%, testing - 10-20%)
'''

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

# function for loading the dataset and variables
def load_data():
    df = pd.read_csv("../data/Basketball_Training_Movement_Biomechanics_Dataset.csv")
    X = df[[
        "movement_type", "hip_flexion_angle_deg", "hip_abduction_angle_deg", 
        "knee_flexion_angle_deg", "ankle_flexion_angle_deg", "shoulder_flexion_angle_deg", 
        "shoulder_abduction_angle_deg", "elbow_flexion_angle_deg", "wrist_flexion_angle_deg", 
        "trunk_flexion_angle_deg", "hip_angular_velocity_deg_s", "knee_angular_velocity_deg_s", 
        "ankle_angular_velocity_deg_s", "shoulder_angular_acceleration_deg_s2", 
        "elbow_angular_acceleration_deg_s2", "wrist_angular_acceleration_deg_s2", 
        "center_of_mass_velocity_m_s", "vertical_jump_height_cm", "ground_contact_time_ms", 
        "movement_duration_ms", "balance_score", "movement_stability_score", 
        "movement_symmetry_pct"
    ]]
    y = df["movement_efficiency_score"]
    return df, X, y

    #function for splitting the data
def split(df, X, y):
    #split data by groups
    #using player_id as the group because don't want the model to learn from that
    groups = df["player_id"]
    
    #split: training - 70%, validation - 15%, testing - 15%
    #outer split for training and validation/testing
    outer = GroupShuffleSplit(n_splits=1, train_size=0.70, random_state=42)
    train_idx, temp_idx = next(outer.split(X, y, groups=groups))
    
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_temp, y_temp = X.iloc[temp_idx], y.iloc[temp_idx]
    
    #inner split to divide validation and testing, still don't want to group by player's id
    groups_temp = groups.iloc[temp_idx]
    inner = GroupShuffleSplit(n_splits=1, test_size=0.50, random_state=42)
    val_idx, test_idx = next(inner.split(X_temp, y_temp, groups=groups_temp))
    
    X_val, y_val = X_temp.iloc[val_idx], y_temp.iloc[val_idx]
    X_test, y_test = X_temp.iloc[test_idx], y_temp.iloc[test_idx]
    
    print(f"Training: {X_train.shape[0]} rows | {len(set(groups.iloc[train_idx]))} unique players")
    print(f"Validation: {X_val.shape[0]} rows | {len(set(groups_temp.iloc[val_idx]))} unique players")
    print(f"Testing: {X_test.shape[0]} rows | {len(set(groups_temp.iloc[test_idx]))} unique players")

    return X_train, X_val, X_test, y_train, y_val, y_test