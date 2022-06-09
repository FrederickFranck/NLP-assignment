import pathlib
import pandas as pd
import nlp.keywords as kw

file_keywords = pathlib.Path(__file__).parent / "data/tax_keywords_nl.pkl"
file_scores = pathlib.Path(__file__).parent / "data/tax_docscores_nl.pkl"
file_dataframe = pathlib.Path(__file__).parent / "data/Staatsblad_nl_fr.pkl"

print(file_dataframe)

def main():
    df = pd.read_pickle(file_dataframe)
    print(df)
    kw.create_initial_keywordlist(df, file_keywords,file_scores)


if __name__ == "__main__":
    main()
