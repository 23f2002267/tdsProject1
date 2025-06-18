# Thread Markdown: 169283

---

    ### 💬 Post 1 by @Jivraj  
    **Posted on:** 2025-03-06 13:48 UTC  

    Please post any questions related to Graded Assignment 6 - Data Analysis
Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.
Deadline 2025-03-15T18:30:00Z

    ---

    ### 💬 Post 2 by @Jivraj  
    **Posted on:** 2025-03-06 13:49 UTC  

    

    ---

    ### 💬 Post 3 by @24f2006061  
    **Posted on:** 2025-03-02 11:45 UTC  

    The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?
@carlton

    ---

    ### 💬 Post 4 by @23f2005138  
    **Posted on:** 2025-03-02 11:57 UTC  

    @Jivraj @Saransh_Saini
I have similar concern
For Q1, I used the following code:
print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

And got the following output:
Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

Whereas options are below where none of them are correct.
*🖼️ Image description: That's a multiple choice question.  The options present four different metrics (Mileage, AvgDistance, Mileage, EngineCapacity) with associated numerical values. The second option, 'AvgDistance: -0.05', is selected.*image281×219 9.1 KB
Whereas for Q2 (Punjab and Yamaha) I used the following code:
print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

and got the following answers:
Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).
*🖼️ Image description: That's a screenshot of a multiple-choice question or selection list.  The options show different values for 'Mileage', 'AvgDistance', and 'EngineCapacity'.  One option, 'Mileage: 0.24', is selected.*image278×216 9.19 KB

    ---

    ### 💬 Post 5 by @carlton  
    **Posted on:** 2025-03-04 10:11 UTC  

    @24f2006061 We are looking into it. We will update based on our analysis. Thanks for letting us know.
Kind regards

    ---

    ### 💬 Post 6 by @AbhinavOhri  
    **Posted on:** 2025-03-03 18:06 UTC  

    I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one
*🖼️ Image description: The image shows a multiple choice question about determining the key factors influencing motorcycle resale value in Delhi.  The choices are Pearson correlation coefficients for mileage, average daily distance, and engine capacity, with engine capacity (0.13) being the selected answer.*image1383×263 25 KB

    ---

    ### 💬 Post 7 by @24ds3000090  
    **Posted on:** 2025-03-07 17:12 UTC  

    Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. @carlton @Jivraj @Saransh_Saini

    ---

    ### 💬 Post 8 by @23f2003413  
    **Posted on:** 2025-03-08 15:17 UTC  

    Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out @carlton !

    ---

    ### 💬 Post 9 by @23ds2000092  
    **Posted on:** 2025-03-10 07:56 UTC  

    I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

    ---

    ### 💬 Post 10 by @21f2000709  
    **Posted on:** 2025-03-11 06:42 UTC  

    Any updates on these? I am too facing the same issue.
@carlton @Jivraj @Saransh_Saini

    ---

    ### 💬 Post 11 by @Udipth  
    **Posted on:** 2025-03-11 17:42 UTC  

    In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one
*🖼️ Image description: This is a multiple choice question about determining the key factors influencing motorcycle resale value.  The question asks to use Pearson Correlation Coefficient to evaluate the impact of mileage, average daily distance traveled, and engine capacity on price retention for Yamaha motorcycles in Maharashtra. The options provide correlation coefficients for each factor.  The correct answer is 'Mileage: 0.95'.*image2083×575 47.6 KB

    ---

    ### 💬 Post 12 by @23f2003413  
    **Posted on:** 2025-03-12 03:42 UTC  

    Kindly update us regarding the status of Q1 & Q2 @carlton @Jivraj

    ---

    ### 💬 Post 13 by @lakshaygarg654  
    **Posted on:** 2025-03-12 11:29 UTC  

    @Jivraj @carlton @Saransh_Saini
Dear TDS Team,
There are multiple issues in Graded Assignment 6 that require urgent attention:

Questions 1 and 2, along with their options, are ambiguous.
In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.
Thank you for your support.

    ---

    ### 💬 Post 14 by @21f2000709  
    **Posted on:** 2025-03-12 13:30 UTC  

    Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.
For instance:

forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

    ---

    ### 💬 Post 15 by @lakshaygarg654  
    **Posted on:** 2025-03-12 14:11 UTC  

    Let’s wait for their response.
I submitted nearby option for Q3 and Q4

    ---

    ### 💬 Post 16 by @23f3001745  
    **Posted on:** 2025-03-12 14:36 UTC  

    @Jivraj @carlton @Saransh_Saini
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).
Thanks

    ---

    ### 💬 Post 17 by @Jivraj  
    **Posted on:** 2025-03-13 09:47 UTC  

    Hi @all
Question intends you to select most correlated one.
Select option which is absolute highest.

    ---

    ### 💬 Post 18 by @Sunil_mv  
    **Posted on:** 2025-03-14 14:30 UTC  

    @Jivraj  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

    ---

    ### 💬 Post 19 by @23f3001601  
    **Posted on:** 2025-03-14 16:06 UTC  

    *🖼️ Image description: The image shows a multiple-choice question about analyzing factors influencing motorcycle resale value in Maharashtra for Honda motorcycles.  The question asks to use Pearson Correlation Coefficient to evaluate the impact of mileage, average daily distance traveled, and engine capacity on price retention.  The correct answer is a negative correlation between mileage and price retention (-0.04).*image1318×377 34.2 KB
what to do if 3 options have same value -0.04 and all are correct?

    ---

    ### 💬 Post 20 by @23f2005471  
    **Posted on:** 2025-03-15 05:54 UTC  

    @carlton @Jivraj
My question 7 for GA6 is :
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance
Whose options provided are :
10418 meters
12287 meters
10965 meters
11149 meters
However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)
I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)
Kindly look into the question, and let me know about the same (the destination from central command post)

    ---

    ### 💬 Post 21 by @21f2000709  
    **Posted on:** 2025-03-15 06:40 UTC  

    Have you succeeded in running the shape file for Q10? It seems to have some error.
@lakshaygarg654

    ---

    ### 💬 Post 22 by @lakshaygarg654  
    **Posted on:** 2025-03-15 06:52 UTC  

    No,
I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

    ---

    ### 💬 Post 23 by @21f2000709  
    **Posted on:** 2025-03-15 07:29 UTC  

    I  downloaded the complete shape file zip from the census.gov site.
Here is the link: https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip
It works fine in QGIS.
@lakshaygarg654

    ---

    ### 💬 Post 24 by @22f3001315  
    **Posted on:** 2025-03-15 07:50 UTC  

    they have not provide all the files needed to read that shp file in the question .
but your link includes them. thanks…

    ---

    ### 💬 Post 25 by @lakshaygarg654  
    **Posted on:** 2025-03-15 09:26 UTC  

    I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.
Thanks for sharing.

    ---

    ### 💬 Post 26 by @Rishabh2  
    **Posted on:** 2025-03-15 15:30 UTC  

    My question 9 for GA6 is :
@carlton @Jivraj @Saransh_Saini
*🖼️ Image description: The image shows Python code that calculates and prints the optimal evacuation sequence for four communities to a central command post based on their distances.  The code uses the `haversine` library to calculate distances from coordinates and then sorts them to display the closest communities first.*Screenshot 2025-03-15 205444878×668 38.1 KB
*🖼️ Image description: This is a multiple choice question about finding the optimal evacuation sequence for four communities using a "nearest community first" strategy.  The question provides the coordinates of each community and a central command post.  The choices present different possible evacuation sequences.  A small portion of Python code is also visible at the bottom.*Screenshot 2025-03-15 2054561333×366 45.8 KB
I solved it in colab but options are getting mismatched there…kindly clarify this issue..

    ---

    ### 💬 Post 28 by @Sunil_mv  
    **Posted on:** 2025-03-15 15:45 UTC  

    for the above question the options are None of these are matching and answer is around 11.5 kms
3848 meters
6265 meters
4110 meters
5106 meters

    ---

    ### 💬 Post 29 by @24ds3000028  
    **Posted on:** 2025-03-15 18:10 UTC  

    For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are
6069 meters
7687 meters
6106 meters
7035 meters
@carlton @Jivraj

    ---

    ### 💬 Post 30 by @23f2000573  
    **Posted on:** 2025-03-16 03:40 UTC  

    @carlton @Jivraj @Saransh_Saini
for question 4, i have tried =forecast and also =forecast.ets, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.
for question 7, none of the options match. I am selecting the MOST ACCURATE among the given options. Hope, it is correct

    ---

    ### 💬 Post 31 by @23f2003413  
    **Posted on:** 2025-03-16 08:26 UTC  

    Can anyone help me out on how to approach and solve the 10th question please!?

    ---

    ### 💬 Post 32 by @lakshaygarg654  
    **Posted on:** 2025-03-16 14:22 UTC  

    Check the distances of other locations from the central location. One student found Question 7 of the GA6 Option Set based on the distances of other points, which do not match the requirements of Question 7.

    ---

    ### 💬 Post 33 by @vidushi  
    **Posted on:** 2025-03-16 15:42 UTC  

    i have the same issue

    ---

    ### 💬 Post 34 by @vidushi  
    **Posted on:** 2025-03-16 15:43 UTC  

    yes i have the same issue
and i got the same answer and am give the same options
@carlton sir what to do?

    ---

    ### 💬 Post 35 by @vidushi  
    **Posted on:** 2025-03-16 16:00 UTC  

    @Jivraj @Saransh_Saini
For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are
6069 meters
7687 meters
6106 meters
7035 meters

    ---

    ### 💬 Post 36 by @Muthupalaniappan  
    **Posted on:** 2025-03-16 18:33 UTC  

    Hello Sir,
Can you please check if this is the right answer. As per email received from @carlton sir we should select the absolute maximum value.
*🖼️ Image description: This is a multiple choice question about determining the key factors influencing motorcycle resale value.  The user incorrectly answered a question about the correlation between different factors (mileage, average daily distance traveled, engine capacity) and price retention for Royal Enfield motorcycles in Uttar Pradesh, using the Pearson Correlation Coefficient. The correct answer, "EngineCapacity: 0.09," is shown at the bottom.*image978×393 23.3 KB
Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.
For the first question the correlation matrix is as follows,
*🖼️ Image description: A correlation matrix heatmap is shown, displaying the correlation coefficients between four variables: mileage (km/l), average daily distance (km), engine capacity (cc), and price retention (%).  The color scale represents the strength and direction of the correlation, with darker reds indicating a strong positive correlation and darker blues a strong negative correlation.*image748×431 17.5 KB
So shouldn’t it be -0.13?

    ---

    ### 💬 Post 37 by @carlton  
    **Posted on:** 2025-03-17 03:43 UTC  

    Thanks for the colour picture.
If you read the aforementioned email…
*🖼️ Image description: An email clarifies that questions 1 and 2 of GA6 were unclear.  The correct answer is the absolute maximum correlation coefficient.  Students are assured their scores will be corrected on the dashboard if they chose the correct answer, despite potential initial incorrect marking.*Screenshot 2025-03-17 at 9.09.55 am1760×632 65.4 KB
Kind regards (in colour *🖼️ Image description: That's a yellow emoticon with a wide smile and one eye closed in a wink.*)

    ---

    ### 💬 Post 38 by @Sunil_mv  
    **Posted on:** 2025-03-18 17:07 UTC  

    Thank you sir. i have got questions 1 and 2 both marked as 0.
*🖼️ Image description: This is a multiple choice question testing understanding of Pearson correlation coefficient.  The question asks to identify the key factor influencing motorcycle resale value in Maharashtra using provided data. The correct answer is 'Mileage: 0.03'.*image962×459 29.1 KB
In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.
I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.
|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||
-0.026685695
|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||
0.003953219
|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||
-0.010839295
|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||
0.029128825
|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||
0.013019585
|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||
-0.056866212

    ---

    ### 💬 Post 39 by @Sunil_mv  
    **Posted on:** 2025-03-18 17:14 UTC  

    @Jivraj @carlton
Dear sirs,
I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.
*🖼️ Image description: This is a multiple-choice question about calculating the distance between two points using the Haversine formula.  The question describes a wildfire emergency and the need to determine the most efficient evacuation route for four communities.  The correct answer is 5106 meters.*image935×529 40.1 KB

    ---

    ### 💬 Post 40 by @23f2005471  
    **Posted on:** 2025-03-19 17:09 UTC  

    @carlton @Jivraj
I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect
My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance
10418 meters
12287 meters
10965 meters
11149 meters
Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)
Also, my question 4 was :
As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.
134483
94774
150666
199711
Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect
So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)
Kindly look into it
Thanks and Regards

    ---

    ### 💬 Post 41 by @23f1001231  
    **Posted on:** 2025-03-20 14:49 UTC  

    @carlton @Jivraj @Saransh_Saini
In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.
*🖼️ Image description: This is a multiple choice question that asks to predict the 2027 resale value of a specific motorcycle model using a forecasting model based on historical data.  The user incorrectly answered and received a score of 0.*image1227×446 24 KB

    ---

    ### 💬 Post 43 by @Jivraj  
    **Posted on:** 2025-03-22 12:34 UTC  

    @all
we are looking into problems with question 4, 6 and 10.

    ---

    ### 💬 Post 44 by @swatikap  
    **Posted on:** 2025-04-11 07:29 UTC  

    Hi,
Have the corrections been done on GA6 marks?

    ---

    ### 💬 Post 45 by @Jivraj  
    **Posted on:** 2025-04-11 09:33 UTC  

    Yes, corrections have been done in Ga6 marks.

    ---

    ### 💬 Post 46 by @swatikap  
    **Posted on:** 2025-04-11 16:31 UTC  

    Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

    