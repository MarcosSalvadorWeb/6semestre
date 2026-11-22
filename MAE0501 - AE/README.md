# Projeto MAE0501: Prevendo avaliações de filmes

## Requirements

```bash
python -m pip install -r requirements.txt
```

## Resultados

RMSE por Validação Cruzada 5-fold 3 vezes em `pure_train`;

| Model | CV RMSE | SE | Variables | Hold-out RMSE | Difference |
|---|---:|---:|---|---:|---:|
| Best MLP [128, 64] alpha=0.26 (Variáveis Transformadas) | 0.4984 | 0.0035 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5063 | 0.0079 |
| XGBoost (Variáveis Transformadas) | 0.5105 | 0.0034 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5123 | 0.0018 |
| LightGBM (Variáveis Transformadas) | 0.5146 | 0.0032 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5165 | 0.0019 |
| MLP ReLU (128, 64) alpha=0.01 (Variáveis Transformadas) | 0.5377 | 0.0042 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5311 | -0.0066 |
| SVR (Variáveis Transformadas) | 0.5537 | 0.0047 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5529 | -0.0008 |
| Random Forest (Variáveis Transformadas) | 0.5708 | 0.0030 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5611 | -0.0097 |
| Regressão ordinal (Variáveis Transformadas) | 0.6243 | 0.0039 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6189 | -0.0054 |
| Linear (Variáveis Transformadas) | 0.6347 | 0.0035 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6211 | -0.0136 |
| KNN - k = 10 (Variáveis Transformadas) | 0.6558 | 0.0042 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6507 | -0.0051 |
| Regressão LASSO (Variáveis Transformadas) | 0.6585 | 0.0025 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6434 | -0.0151 |
| Linear | 0.8270 | 0.0028 | user_avg_stars, user_n_ratings, age, share_action, share_comedy, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama | 0.8063 | -0.0207 |
| K-Means + K-NN nos centroides (Variáveis Transformadas) | 1.0936 | 0.0023 | user_avg_stars, log_user_n_ratings, age, share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 1.0847 | -0.0089 |
| Constante | 1.1678 | 0.0016 | user_avg_stars, user_n_ratings, age, share_action, share_comedy, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama | 1.1559 | -0.0119 |
