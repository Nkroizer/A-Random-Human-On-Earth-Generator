# A Random Human on Earth


As a hobbyist writer and a CS major, I want to create a set of tools to help ease the process of writing.

This tool was created to generate a truly random person on Earth.

There are approximately 8.1 billion people on earth as of today (January 7th, 2024). So, there are a large variety of people to select from.

1. The first order of business was to generate a country on earth with a respectable probability for each country (I.E. India has 17.8% probability, China has 17.7%, the US has 4.2 and so forth) [The source for the information about world population percentages] [1]
2. After I had the country, I got the average life expectancy of people of that specific country (Hong Kong 85.83 years, Macao 85.51 years, Japan 84.95 years, and so on) [The source for the information about life expectancy by country] [2]
3. Once I had the average life expectancy, I generated a random approximation of that person's age in the range of the average life expectancy with a padding of 0-20 extra years.
4. Now I have the country, and the approximate age, so I could generate the person's sex using the male/female sex ratio by country and age groups (children 0-14, adults 15-64, elderly 65+) [The source for the information about sex ratio by country and age group] [3]
5. If the person is younger than 65, the approximate age becomes the actual age, and if he is older, then I generate a random age between 65 and the respectable life expectancy that is specific to that country and sex with a padding of 0-20 extra years [The source for the information about life expectancy by country and by sex group] [2]
6. Finally, I used an API to generate a First Name and Last Name based on the person's sex and country [The source for the API] [4]

----

This is the README file for the project.


[src]: https://github.com/pypa/sampleproject
[1]: https://www.worldometers.info/world-population/
[2]: https://www.worldometers.info/demographics/life-expectancy/
[3]: https://statisticstimes.com/demographics/countries-by-sex-ratio.php
[4]: https://api.parser.name
