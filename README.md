# Fake News Detection(Romanian)
Project for the **NLP** course at the [Faculty of Computer Science Iași](https://www.info.uaic.ro/en/home-page-2/).
## Team
  * [Ioana Parfene](https://github.com/IoanaParfene)
  * [Codrin Donciu](https://github.com/Codrinator)
  * [Alexandru Panainte]()
## Implementation Status
### Gathered Data 
&nbsp;&nbsp;&nbsp;&nbsp; **True News**(200 000 words)
  * [ProTV](https://stirileprotv.ro/) - 42,000 
  * [Digi24](https://www.digi24.ro/) -  70,000
  * [Libertatea](https://www.libertatea.ro/) - 42,000 
  * [Realitatea](https://www.realitatea.net/) - 46,000
  
&nbsp;&nbsp;&nbsp;&nbsp; **Fake News**(200 000 words)
  * [TimesNewRoman](https://www.timesnewroman.ro/) - 8,000
  * [Cațavencii](https://www.catavencii.ro/) - 99,000
  * [7lucruri](https://7lucruri.ro/) - 56,000
  * [TimpuriGrele](https://www.timpurigrele.ro/) - 37,000

### Preprocessed data
&nbsp;&nbsp;&nbsp;&nbsp;**1) Lowercased** the text bodies

&nbsp;&nbsp;&nbsp;&nbsp;**2) Tokenized** each news article

&nbsp;&nbsp;&nbsp;&nbsp;**3) Stemmed** romanian words

&nbsp;&nbsp;&nbsp;&nbsp;**4) Vocabularized** both news categories

<hr style="border:2px solid gray"> </hr>

## Progress
### Week 3

&nbsp;&nbsp;&nbsp;&nbsp;**Ioana**
  * Added **7lucruri** and **TimpuriGrele** articles
  * Created **vocabularies** for the fake/true news text bodies
  * Cleaned up **code**
  
&nbsp;&nbsp;&nbsp;&nbsp;**Codrin**
  * Added **Digi24** articles
  * **Stemmed** the romanian words
  * Solved romanian **encoding** issues
  
&nbsp;&nbsp;&nbsp;&nbsp;**Alex**
  * Added **Realitatea** articles
  * **Tokenized** the news articles
  * Created data **storage** files
