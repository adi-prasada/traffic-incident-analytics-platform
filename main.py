from src.analytics import generate_synthetic_incidents, RoadSafetyAnalytics

def main():
    print("=== Traffic Incident & Blackspot Analytics Platform ===")
    df = generate_synthetic_incidents(2000)
    print("Ingested standardized incident records: " + str(len(df)))
    
    platform = RoadSafetyAnalytics(df)
    ranked = platform.rank_blackspots()
    
    print("\nCorridor Blackspot Risk Ranking:")
    print(ranked.to_string(index=False))

if __name__ == '__main__':
    main()
