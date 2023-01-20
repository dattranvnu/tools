library(rvest)
links = paste(paste("https://www.codecademy.com", read_html("0-links.html") %>% html_nodes(xpath='//a[@class="e14vpv2g1 gamut-1ssowio-ResetElement-Anchor-AnchorBase e1bhhzie0"] | //a[@class="e14vpv2g1 gamut-1m5v0xn-ResetElement-Anchor-AnchorBase e1bhhzie0"]') %>% html_attr('href'),sep=''),
collapse=',\n')

fileConn<-file("0-links.txt")
writeLines(links, fileConn)
close(fileConn)