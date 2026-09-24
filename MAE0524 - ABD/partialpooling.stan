data {

  int<lower=1> N;
  int<lower=0> y[N];
  int<lower=0> n[N];

}

parameters {

  real<lower=0> alpha;
  real<lower=0> beta;

  vector<lower=0,upper=1>[N] theta;

}

model {

  alpha ~ gamma(1,1);
  beta  ~ gamma(1,1);

  theta ~ beta(alpha,beta);

  y ~ binomial(n, theta);

}
