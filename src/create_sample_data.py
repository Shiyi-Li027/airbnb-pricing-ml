import os
import pandas as pd


RAW_DATA_PATH = "data/listings_20250301.csv"
OUTPUT_DIR = "sample_data"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "sample_listings.csv")

SAMPLE_SIZE = 100
RANDOM_STATE = 42

COLUMNS_TO_KEEP = [
    "id",
    "host_id",
    "host_is_superhost",
    "neighbourhood_cleansed",
    "neighbourhood_group_cleansed",
    "latitude",
    "longitude",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "amenities",
    "price",
    "number_of_reviews",
    "review_scores_rating",
    "availability_30",
    "availability_365",
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(RAW_DATA_PATH)

    missing_cols = [col for col in COLUMNS_TO_KEEP if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in raw dataset: {missing_cols}")

    sample = (
        df[COLUMNS_TO_KEEP]
        .drop_duplicates()
        .sample(n=min(SAMPLE_SIZE, len(df)), random_state=RANDOM_STATE)
    )

    sample.to_csv(OUTPUT_PATH, index=False)

    print(f"Sample data saved to: {OUTPUT_PATH}")
    print(f"Sample shape: {sample.shape}")


if __name__ == "__main__":
    main()