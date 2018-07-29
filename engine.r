# Clean Data 
# 1.set H or A; 2. set date format; 3. calculate the 'Four Factors' difference between the team and its opponent.
# table is in the format of "TeamName_0"

cleanTable <- function(table){
  newtable <- table
  newtable$HorA <- ifelse(newtable$HorA == '', 'H','A')
  newtable$Date <- as.Date(newtable$Date,format = '%m/%d/%Y')
  newtable$diff_eFG <- (newtable$`eFG%`-newtable$`OppeFG%`) * 100
  newtable$diff_TOV <- newtable$`TOV%`-newtable$`OppTOV%`
  newtable$diff_ORB <- newtable$`ORB%`-newtable$`OppDRB%`
  newtable$diff_FT <- (newtable$`FT/FGA`-newtable$`OppFT/FGA`) * 100
  newtable$diff_score <- newtable$Tm - newtable$Opp_1
  return(newtable)
}


# Linear regression: diff_score ~ Four factors. Ideally we need to train with as much data as possible
# As a demo, I trained the model with only two teams' data
trainModel <- function(newtables){
  fit <- lm(diff_score ~ diff_eFG + diff_TOV + diff_ORB + diff_FT, data = newtables)
  return(fit$coefficients)
}

# Calculate Team's past performance, filtered on date, teamname and HomeOrAway
calTeamPastStats <- function(date,file,HorA){
  newtable <- read.csv(file, na = "empty")
  a<-list()
  subdf <- newtable[newtable$Date < as.Date(date,format = '%m/%d/%Y') & newtable$HorA == HorA,]
  a$normPar_eFG <- c(mean(subdf$diff_eFG), var(subdf$diff_eFG))
  a$normPar_TOV <- c(mean(subdf$diff_TOV), var(subdf$diff_TOV))
  a$normPar_ORB <- c(mean(subdf$diff_ORB), var(subdf$diff_ORB))
  a$normPar_FT <- c(mean(subdf$diff_FT), var(subdf$diff_FT))
  return(a)
}

# Simulation
simulation <- function(date,HomeTeam,AwayTeam){
  temp <- read.csv('temp.csv', na = "empty")
  param_list <- trainModel(temp)
  statsH <- calTeamPastStats(date,HomeTeam,'H')
  statsA <- calTeamPastStats(date,AwayTeam,'A')
  eFG <- rnorm(100,mean = statsH$normPar_eFG[1], sd = sqrt(statsH$normPar_eFG[2])) - rnorm(100*10000,mean = statsA$normPar_eFG[1], sd = sqrt(statsA$normPar_eFG[2]))
  TOV <- rnorm(100,mean = statsH$normPar_TOV[1], sd = sqrt(statsH$normPar_TOV[2])) - rnorm(100*10000,mean = statsA$normPar_TOV[1], sd = sqrt(statsA$normPar_TOV[2]))
  ORB <- rnorm(100,mean = statsH$normPar_ORB[1], sd = sqrt(statsH$normPar_ORB[2])) - rnorm(100*10000,mean = statsA$normPar_ORB[1], sd = sqrt(statsA$normPar_ORB[2]))
  FT <- rnorm(100,mean = statsH$normPar_FT[1], sd = sqrt(statsH$normPar_FT[2])) - rnorm(100*10000,mean = statsA$normPar_FT[1], sd = sqrt(statsA$normPar_FT[2]))
  pred_scorediff <- param_list[1] + param_list[2] * eFG + param_list[3]* TOV + param_list[4]* ORB + param_list[5] * FT
  winRatio_H <- sum(pred_scorediff>0)/1000000
  return(winRatio_H)
}


# Return T or F to tell whether to place the bets
BetorNot <- function(winRatio_H, marketOdds){
  key = F
  EV <- winRatio_H*marketOdds - (1-winRatio_H)
  if(EV>0.05){
    key = T
  }
  return(key)
}

# Return the balance after knowing the betting results
pnl <- function(balance, betAmount, marketOdds, gameResult){
  if(gameResult == 'W'){
    profit <- betAmount * marketOdds
  }
  else{
    profit <- -betAmount
  }
  balance <- balance + profit
}
