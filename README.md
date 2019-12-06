# DataScience_Project1
Jimmy Wrangler: Traveling the world on a mission to discover new data

Steps:
1.	Load data into data frame <br />
a.	Movie <br />
b.	Box Office <br />
2.	Merge datasets <br />
a.	Merge based on movie title <br />
3.	Clean data <br />
a.	Check for NAN values <br />
b.	Make sure that years match <br />
4.	Feature Engineering <br />
a.	Check if movie years from both data sets are the same <br />
b.	Add countries that movies filmed with <br />
5.	Visualization <br />
a.	Seaborn graphs <br />
b.	Seaborn heat maps <br />
6.	Conclusions:

I merged two datasets together that had box office data and film information data.
Since majority of my data occurred within last ten years, I decided to investigate the 
data from the 2000s. Through investigating this data, I found that rank and lifetime gross 
are exponentially related where first ranked yields a higher Lifetime gross for domestic 
US sales. I also found that moves that have a higher lifetime gross are not often ranked
very well by IMDB. They are usually ranked at about a 6/10. I also found that the fantasy
and super hero genres have the highest lifetime gross in the 2000s. This is probably due to
franchises like MARVEL and Harry Potter. I used heat maps to look for correlations between rank,
lifetime gross, duration, and votes and also between which countries. I found a surprising but
fairly strong correlation between lifetime gross and duration of the movie, and that the United
States does not usually film with other countries.
