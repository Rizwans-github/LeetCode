import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df = df.drop_duplicates('author_id')
    df = df.sort_values('author_id', ascending = True )
    df['id'] = df['author_id']
    return df[['id']]