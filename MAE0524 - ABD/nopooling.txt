data {

  int<lower=1> N;
  int<lower=0> y[N];
  int<lower=0> n[N];

}

parameters {

  vector<lower=0,upper=1>[N] theta;

}

model {

  theta ~ beta(1,1);

  y ~ binomial(n, theta);

}
