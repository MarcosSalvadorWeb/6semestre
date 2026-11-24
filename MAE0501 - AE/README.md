# Projeto MAE0501: Prevendo avaliações de filmes

## Requirements

```bash
python -m pip install -r requirements.txt
```

## Resultados

RMSE por validação cruzada estratificada (5 folds, repetida 3 vezes) em `pure_train`; hold-out com 20% das linhas,
separado antes de qualquer análise. Todas as partições e modelos aleatórios têm semente fixa, então
rodar o notebook do início ao fim reproduz exatamente esta tabela.

| Model | CV RMSE | SE | Variables | Hold-out RMSE | Difference |
|---|---:|---:|---|---:|---:|
| Best MLP (128, 64) alpha=0.26 | 0.4940 | 0.0031 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5032 | 0.0092 |
| XGBoost (tunado) | 0.5066 | 0.0030 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5087 | 0.0021 |
| MLP ReLU (128, 64) alpha=0.01 | 0.5283 | 0.0041 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5382 | 0.0099 |
| LightGBM | 0.5304 | 0.0035 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5267 | -0.0037 |
| SVR | 0.5486 | 0.0043 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5540 | 0.0054 |
| Random Forest | 0.5709 | 0.0030 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5611 | -0.0098 |
| XGBoost (padrão) | 0.5723 | 0.0038 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5679 | -0.0044 |
| Regressão ordinal | 0.5867 | 0.0034 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5923 | 0.0056 |
| Linear stepwise (variáveis transformadas) | 0.5941 | 0.0032 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5914 | -0.0027 |
| Linear | 0.5945 | 0.0032 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.5914 | -0.0031 |
| Regressão LASSO | 0.6171 | 0.0027 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6150 | -0.0021 |
| Linear (Variáveis originais + ln(share_match)) | 0.6185 | 0.0027 | user_avg_stars, user_n_ratings, age, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama, share_match | 0.6175 | -0.0010 |
| KNN - k = 10 | 0.6393 | 0.0039 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 0.6441 | 0.0048 |
| Linear (Variáveis originais + share_match) | 0.6578 | 0.0027 | user_avg_stars, user_n_ratings, age, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama, share_match | 0.6453 | -0.0125 |
| Linear stepwise (variáveis originais) | 0.8264 | 0.0028 | user_avg_stars, user_n_ratings, age, share_action, share_comedy, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama | 0.8062 | -0.0202 |
| Linear (Variáveis originais) | 0.8270 | 0.0028 | user_avg_stars, user_n_ratings, age, share_action, share_comedy, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama | 0.8063 | -0.0207 |
| K-Means + K-NN nos centroides | 1.0984 | 0.0028 | user_avg_stars, log_user_n_ratings, age, ln_share_match, age_x_year, age_at_release, movie_avg_stars, log_movie_n_ratings, genre_comedy, genre_drama | 1.0776 | -0.0208 |
| Constante | 1.1678 | 0.0016 | user_avg_stars, user_n_ratings, age, share_action, share_comedy, movie_avg_stars, movie_n_ratings, release_year, genre_comedy, genre_drama | 1.1559 | -0.0119 |
