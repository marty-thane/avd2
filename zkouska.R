library(expm)

P_t <- function(t) {
  matrix(c(0.6 + 0.4 * t, 0.3 - 0.3 * t, 0.1 - 0.1 * t,
           0.2 + 0.8 * t, 0.6 - 0.6 * t, 0.2 - 0.2 * t,
           0.1 + 0.9 * t, 0.2 - 0.2 * t, 0.7 - 0.7 * t), 
         nrow = 3, byrow = TRUE)
}

tridy <- c(0, 30000, 100000)
pocet_obyvatel <- 50000000

uhrnny_prijem_simul <- function(t, opakovani = 1000) {
  P <- P_t(t)
  stavy <- sample(1:3, pocet_obyvatel, replace = TRUE)
  
  for (i in 1:opakovani) {
    for (j in 1:pocet_obyvatel) {
      pst_prechodu <- P[stavy[j], ]
      stavy[j] <- sample(1:3, 1, prob = pst_prechodu)
    }
  }
  
  prijmy <- tridy[stavy]
  sum(prijmy)
}

tvec_simul <- seq(0, 1, by = 0.05)
prijmy_simul <- sapply(tvec_simul, uhrnny_prijem_simul)
laffer_simul <- prijmy_simul * tvec_simul

par(mfrow = c(1, 2), mar = c(4, 4, 2, 1))
plot(tvec_simul, prijmy_simul, type = "l", xlab = "Daňová sazba", ylab =
     "Úhrnný hrubý příjem", main = "Úhrnný hrubý příjem (simulace)")
plot(tvec_simul, laffer_simul, type = "l", xlab = "Daňová sazba", ylab =
     "Úhrnný daňový výnos", main = "Lafferova křivka (simulace)")

uhrnny_prijem_anal <- function(t, opakovani = 1000) {
  P <- P_t(t) %^% opakovani
  stavy <- sample(1:3, pocet_obyvatel, replace = TRUE)
  
  for (i in 1:pocet_obyvatel) {
    pst_prechodu <- P[stavy[i], ]
    stavy[i] <- sample(1:3, 1, prob = pst_prechodu)
  }
  
  prijmy <- tridy[stavy]
  sum(prijmy)
}

tvec_anal <- seq(0, 1, by = 0.05)
prijmy_anal <- sapply(tvec_anal, uhrnny_prijem_anal)
laffer_anal <- prijmy_anal * tvec_anal

par(mfrow = c(1, 2), mar = c(4, 4, 2, 1))
plot(tvec_anal, prijmy_anal, type = "l", xlab = "Daňová sazba", ylab = "Úhrnný
     hrubý příjem", main = "Úhrnný hrubý příjem (analyticky)")
plot(tvec_anal, laffer_anal, type = "l", xlab = "Daňová sazba", ylab = "Úhrnný
     daňový výnos", main = "Lafferova křivka (analyticky)")
