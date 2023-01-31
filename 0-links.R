library(rvest)
library(tidyverse)
links = paste(paste("https://www.codecademy.com", read_html("0-links.html") %>% html_nodes(xpath='//a') %>% html_attr('href'),sep=''),
collapse=',\n')

fileConn<-file("0-links.txt")
writeLines(links, fileConn)
close(fileConn)