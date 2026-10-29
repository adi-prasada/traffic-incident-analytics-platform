from src.analytics import generate_synthetic_incidents, RoadSafetyAnalytics

def test_blackspot_ranking():
    df = generate_synthetic_incidents(100)
    sa = RoadSafetyAnalytics(df)
    res = sa.rank_blackspots()
    assert len(res) > 0
    assert "total_hazard_score" in res.columns
