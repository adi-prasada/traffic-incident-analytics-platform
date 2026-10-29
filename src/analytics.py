import pandas as pd
import numpy as np

def generate_synthetic_incidents(num: int = 1500) -> pd.DataFrame:
    np.random.seed(99)
    corridors = ["Corridor_A1_Pantura", "Corridor_B4_Southern", "Toll_KM_45_Inner", "Toll_KM_120_Cikampek", "Arterial_Jalan_Sudirman"]
    severities = ["MINOR_DAMAGE", "MODERATE_INJURY", "FATALITY", "SEVERE_INJURY"]
    
    data = []
    for i in range(num):
        sev = np.random.choice(severities, p=[0.60, 0.25, 0.05, 0.10])
        weight = 1 if sev == "MINOR_DAMAGE" else (3 if sev == "MODERATE_INJURY" else (5 if sev == "SEVERE_INJURY" else 10))
        data.append({
            "incident_id": "INC-" + str(50000 + i),
            "corridor": np.random.choice(corridors),
            "severity": sev,
            "hazard_weight": weight,
            "hour_of_day": int(np.random.choice(range(24))),
            "vehicle_count": int(np.random.choice([1, 2, 3, 4], p=[0.3, 0.5, 0.15, 0.05]))
        })
    return pd.DataFrame(data)

class RoadSafetyAnalytics:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def rank_blackspots(self) -> pd.DataFrame:
        agg = self.df.groupby("corridor").agg(
            total_incidents=("incident_id", "count"),
            total_hazard_score=("hazard_weight", "sum"),
            avg_vehicles=("vehicle_count", "mean")
        ).reset_index()
        agg = agg.sort_values(by="total_hazard_score", ascending=False)
        return agg
