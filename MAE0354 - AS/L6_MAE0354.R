# Questão 03 - MAE0354
library(readxl)
dados = read_xls(path = "Documents/viarapidareduzido1.xls")
head(dados)

## Letra a)
library("survival")
modelo_cox  = coxph(Surv(DIAS,DELTA) ~ Protocolo + IDADE + SEXO + TIPAC, data = dados)
summary(modelo_cox)

## Letra b)

# Coeficientes estimados para o modelo de Cox
coef(modelo_cox)

# Paciente no protocolo convencional (0)
paciente_convencional <- data.frame(
  Protocolo = 0,
  IDADE = 60,
  SEXO = 1,
  TIPAC = 1
)

# Paciente no protocolo de via rápida (1)
paciente_rapida <- data.frame(
  Protocolo = 1,
  IDADE = 60,
  SEXO = 1,
  TIPAC = 1
)

library(survival)
library(survminer)
library(ggplot2)
library(patchwork)

# Estimar as curvas pelo modelo de Cox
curva_convencional <- survfit(
  modelo_cox,
  newdata = paciente_convencional,
  conf.type = "log"
)

curva_rapida <- survfit(
  modelo_cox,
  newdata = paciente_rapida,
  conf.type = "log"
)

# Gráfico do protocolo convencional
p1 <- ggsurvplot(
  curva_convencional,
  data = dados,
  conf.int = TRUE,
  color = 
  censor = FALSE,
  legend = "none",
  xlab = "Tempo (dias)",
  ylab = "Probabilidade de sobrevivência",
  title = "Protocolo convencional",
  ggtheme = theme_minimal()
)$plot

# Gráfico do protocolo de via rápida
p2 <- ggsurvplot(
  curva_rapida,
  data = dados,
  conf.int = TRUE,
  censor = FALSE,
  legend = "none",
  xlab = "Tempo (dias)",
  ylab = "Probabilidade de sobrevivência",
  title = "Protocolo de via rápida",
  ggtheme = theme_minimal()
)$plot

# Combinar os gráficos lado a lado
p1 + p2

## Letra c)


## Letra d)