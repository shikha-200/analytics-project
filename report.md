# Understanding Bicycle Theft in Toronto: Trends, Risks, and Solutions

*By: Shikha Rani*

## Introduction
Bicycle theft is a significant issue in urban environments, particularly in cities like Toronto, where cycling is a common mode of transportation. The rising number of bicycle theft incidents poses challenges for cyclists, law enforcement, and urban planners. This study analyzes bicycle theft patterns in Toronto using a dataset from the Toronto Police Service spanning from 2013 to 2022. By employing data-driven methodologies, the study identifies key trends, high-risk areas, and factors contributing to bicycle theft.
Key objectives of the study include identifying temporal and spatial theft patterns, assessing the influence of bike type and cost, and providing recommendations for theft prevention. The insights generated can help law enforcement optimize patrols, assist city planners in designing secure bike parking facilities, and guide cyclists in making informed security choices.

### Research Objectives
The primary objective of this study is to analyze bicycle theft patterns in Toronto using data-driven methodologies. Specific objectives include:
1. Identify Temporal Trends: Examine how bicycle theft incidents vary across different times of the day, days of the week, and seasons.
2. Analyze Spatial Distribution: Identify high-risk neighborhoods and theft hotspots in Toronto.
3. Examine Theft Patterns by Bike Type & Cost: Determine which types and price ranges of bicycles are most frequently stolen.
4. Assess Contributing Factors: Investigate factors influencing bicycle theft, such as location type, security measures, and weather conditions.
5. Develop Theft Prevention Strategies: Provide actionable recommendations for cyclists, law enforcement, and city planners to mitigate bicycle theft.
6. Support Policy & Infrastructure Planning: Offer insights to improve bike security infrastructure and urban planning initiatives.

# Exploratory Data Analysis

**Bar Plot**
- Theft Count vs. Bike Type
  
  For the Theft Count vs. Bike Type chart I created, The bar chart depicts the relationship between different bike types and the count of theft incidents associated with each type. The analysis reveals that mountain bikes (MT) and road bikes (RG) are the most frequently stolen, with theft counts exceeding 10,000 for each category. This suggests their high popularity and potential resale value, making them prime targets for theft. Other bike types, such as recreational bikes (RC) and other unspecified types (OT), also show notable theft frequencies, indicating moderate demand or usage. In contrast, categories like folding bikes (FO), tandem bikes (TA), and racing bikes (TR) exhibit significantly lower theft counts, likely due to their niche usage and lower prevalence in the population. This data emphasizes the need for tailored theft prevention measures based on bike type. For high-risk categories like mountain and road bikes, initiatives such as robust locking mechanisms, secure parking infrastructure, and public education on theft deterrence can be prioritized. Additionally, further investigation into theft patterns specific to these bike types may provide deeper insights for targeted intervention strategies.
- Theft Count vs. Status (Recovered or Not)

  For the Theft Count vs. Status (Recovered or Not) chart I created, I used a bar chart to visually represent the distribution of recovered and non-recovered bicycles in the dataset. Each bar corresponds to one of the two categories (recovered and not recovered) and the height of each bar reflects the number of theft cases in each category. This chart effectively illustrates the disparity between bicycles that have been recovered after theft and those that have not. The visual makes it easy to see whether there is a significant gap between recovery rates, helping to highlight recovery success or challenges. For instance, if the ”Not Recovered” bar is substantially taller, it signals that most stolen bicycles are not recovered, emphasizing a need for improved recovery methods or theft prevention efforts. This simple yet informative visual helps communicate the effectiveness (or lack thereof) of recovery efforts and can guide further investigations into why certain bikes are recovered while others are not. It serves as a powerful tool for policy discussions on enhancing recovery strategies for stolen bicycles.
- Number of Thefts vs. Neighborhood

  For the Number of Thefts vs. Neighborhood chart I created, provides a detailed distribution of bicycle thefts across different neighborhoods, identified by their respective IDs. A clear concentration of theft incidents is observed around neighborhood ID 80, which stands out as a significant hotspot with over 3,500 thefts, far exceeding other areas. This suggests potential underlying factors such as higher population density, more bicycle usage, or inadequate security measures in this neighborhood. Interestingly, the distribution also reveals sporadic spikes in theft counts across other neighborhood IDs, indicating localized patterns of high theft activity. These anomalies could be linked to specific events, infrastructure, or socio-economic factors unique to those areas. The stark contrast between high-theft and low-theft neighborhoods highlights the importance of implementing targeted strategies, such as increased surveillance, public awareness campaigns, and improved bicycle parking infrastructure in theft-prone areas. Moreover, further investigation into the socio-economic and geographical characteristics of high-theft neighborhoods could provide actionable insights for long-term prevention measures.

**Histogram**
- Theft Count vs. Bike Price

  For the Theft Count vs. Bike Price chart I created, I used a histogram to represent the distribution of bicycle prices at the time of theft. In this chart, the x-axis is divided into price ranges (bins), and the y-axis shows the number of thefts that occurred within each price range. The histogram allows for a clear visualization of how frequently bicycles within different price brackets are stolen. For example, it may reveal whether thefts are more common for 7 lower-priced bikes, mid-range bikes, or high-end models. Unlike a bar chart, which compares categories, the histogram groups continuous data (bike prices) into ranges, making it ideal for showing how theft incidents are spread across different price levels. This histogram helps identify patterns in the relationship between bicycle price and theft risk. If the chart shows a peak in the mid-range or high-end price bins, it may indicate that thieves prefer bicycles of a certain value, which can inform both bike owners and policymakers about which types of bicycles are more vulnerable to theft and thus require enhanced security measures
- Theft Count vs. Month

  For the Theft Count vs. Month chart, I used a histogram to display the distribution of bicycle thefts across different months of the year. The x-axis represents the months, while the y-axis shows the number of thefts that occurred during each month. This histogram allows for an analysis of theft patterns over time, helping to identify any seasonal trends or periods of increased theft activity. For example, if the chart shows higher theft counts during the summer months and lower counts in winter, it could indicate that thefts are more common during warmer seasons when more people use bicycles. By visualizing the data in this way, the histogram provides valuable insights into when thefts are most likely to occur, which can help law enforcement, policymakers, and cyclists plan targeted interventions and theft prevention strategies during high-risk months.
- Theft Count vs. Hour of the Day

  The histogram illustrates the distribution of bicycle theft counts across different hours of the day. A clear pattern emerges, showing two distinct peaks in theft activity. The first peak occurs around midnight (hour 0), with over 2,000 incidents, likely due to reduced visibility and fewer witnesses. The second, more significant peak is observed in the evening hours around 8 PM, again surpassing 2,000 thefts, possibly coinciding with the time people return home or park their bicycles in less secure locations. Theft activity is relatively low during early morning hours (around 4-6 AM), likely due to reduced outdoor activity. As the day progresses, thefts gradually increase, with a steady rise observed between 10 AM and late afternoon, reflecting higher bicycle usage during these times. This analysis suggests that targeted interventions, such as increasing surveillance and awareness campaigns during high-risk hours (evenings and late nights), could help reduce bicycle theft. Additionally, promoting secure bicycle storage solutions during these hours may further mitigate theft risks.

**Box Plot**
For the Price of Bicycle chart, I used a box plot to illustrate the distribution of bicycle prices in the dataset. The x-axis represents the bicycle price, while the y-axis displays the frequency or count of bicycles within specific price ranges. The box plot provides a comprehensive summary of the price distribution by highlighting key statistical measures, including the median, quartiles, and potential outliers. The box itself represents the interquartile range (IQR), which contains the middle 50% of the prices, while the line inside the box indicates the median price. The ”whiskers” extend to show the range of the data, excluding outliers, which are plotted as individual points beyond the whiskers [2]. This visualization is particularly useful for understanding the overall distribution of bicycle prices and identifying any skewness or anomalies in the data. For instance, it may reveal whether most bicycles fall within a certain price range or if there are a significant number of high-priced outliers. By using a box plot, we can quickly assess the central tendency and variability of bicycle prices, allowing stakeholders to understand pricing trends in the market. This analysis can inform decisions for both potential buyers and sellers, as well as for policymakers seeking to address issues related to bicycle theft

**Scatter Plot**
This scatter plot provides a comprehensive view of the relationship between bike cost, speed, and type, while also incorporating color as an additional categorical variable. By visualizing these dimensions together, we can identify patterns and correlations, such as: 
- Cost vs. Speed: re higher-cost bicycles generally faster? This relationship can help potential buyers understand the trade-off between cost and performance.
- Type Distribution: How do different bike types distribute in terms of cost and speed? This can reveal trends in specific categories, showing which types are more likely to be high-speed or low-cost.
- Color Preferences: Are certain colors more prevalent among specific types or price ranges? This may provide insights into consumer preferences or market trends. 
Overall, the scatter plot serves as a powerful tool for analyzing the relationships among bicycle attributes, assisting stakeholders in making informed decisions related to purchasing, marketing, and theft prevention strategies.

**Heat Map**
- Year vs Month vs Number of Thefts

  The heat map illustrates the distribution of bicycle thefts across various years and months, highlighting seasonal and temporal trends. The color gradient, ranging from light yellow (low theft count) to dark blue (high theft count), provides a clear visual representation of the intensity of thefts. Key insights from the heat map: 
  - Seasonal Trends: Theft counts peak during the summer months, particularly from June to August, across multiple years. This aligns with increased outdoor activity and bicycle usage during warmer weather.
  - Yearly Trends: Over the years, there has been a noticeable fluctuation in theft counts, with certain years, such as 2018 and 2020, showing higher overall theft activity. These could indicate socio-economic factors, changes in bicycle ownership, or security conditions
  - Decline in Recent Years: A general decline in theft counts is observed in 2022 and 2023, especially during the later months. This may reflect improved preventive measures, changes in bicycle usage, or underreporting.
  - Low Activity Months: The months of December through February consistently show lower theft counts, likely due to reduced bicycle usage during colder weather.
  This analysis suggests the need for targeted theft prevention efforts during high-risk periods, especially in summer months. For law enforcement, focusing patrols and surveillance during these peak months could be effective. For bicycle owners, this insight emphasizes the importance of securing bicycles more rigorously during the summer when theft risk is highest. Additionally, further analysis could investigate the socio-economic and environmental factors contributing to the yearly variations.
- Temporal Heatmap by Hour and Day

  The heatmap visualizes bicycle theft activity based on the hour of the day and the day of the week. Here are some insights based on the graph: 
  - Peak Hours:The highest theft activity appears during the evening hours, particularly around 5 PM to 7 PM. This might correlate with times when people commute home or leave their bicycles unattended.
  - Active Days: Theft activity is consistent across the weekdays but appears to peak on Tuesdays and Fridays, especially during specific hours. These might correspond to work or busy social activity days.
  - Weekend Trends: Compared to weekdays, thefts are lower during the weekends, indicating that fewer people might leave their bikes unattended or that bike usage patterns change on weekends.
  - Early Morning and Late Night: There is significantly lower activity during latenight and early-morning hours (12 AM to 6 AM), which aligns with less public movement during these times.
  - Patterns to Investigate: The concentration of thefts in the evenings suggests opportunistic theft behavior when bicycles are left unattended for longer periods, such as during office hours or social activities. 
  Specific days like Tuesday or Friday might be associated with external events, such as market days or higher foot traffic in certain neighborhoods. 
  This analysis suggests potential actions such as raising awareness of theft-prone times and enhancing security (e.g., bike locks or surveillance) during peak hours to reduce incidents.


# Statistical Analysis

**Methods**
*RandomForest Classifier*
- Chosen due to its ability to handle non-linear relationships and its resistance to
 overfitting with multiple trees and random feature selection.
– The Random Forest model was trained using the features of latitude, longitude, day of the week, month, and weekend status.
– Hyperparameters such as the number of trees (n estimators) were set to 100, and random state was fixed at 42 for reproducibility

*Naive Bayes Classifier*
– Assumes conditional independence between features, making it computationally efficient and simple to implement.
– The Gaussian Naive Bayes variant was used since it is suitable for continuous
 numerical features like latitude and longitude.
– Features were normalized to meet the algorithm’s assumption of normally distributed data.

*Gradient Boosting Classifier*
– Apowerful ensemble method that builds decision trees sequentially, with each tree correcting the errors of its predecessor.
– Implemented using Scikit-learn’s GradientBoostingClassifier.
– Parameters such as the learning rate and the number of estimators were tuned to optimize performance while avoiding overfitting.

*Decision Tree Classifier*
– Asimple yet effective algorithm for classification tasks, which splits data based on feature thresholds to maximize information gain (Gini Impurity).
– Provides interpretable outputs, showing how different features contribute to predictions.

** Result **

The analysis of bicycle theft incidents using four machine learning models—Random Forest, Naive Bayes, Gradient Boosting, and Decision Tree—revealed distinct strengths and weaknesses in predictive performance.
 - Random Forest (Accuracy: 88.113%): Random Forest achieved the highest accuracy, indicating it performs well in capturing patterns and relationships in the data. This result is expected because Random Forest is an ensemble method that combines multiple decision trees, which helps handle overfitting and improves generalization.
 - Naive Bayes (Accuracy: 31.449%): Naive Bayes performed the worst among all models. Its assumptions of feature independence may not align with the data’s realworld correlations. Theft occurrence is likely influenced by several interacting factors (e.g., time, location, season), and Naive Bayes struggles to model these interactions effectively.
 - Gradient Boosting (Accuracy: 56.235%): Gradient Boosting achieved moderate accuracy, outperforming Naive Bayes and Decision Tree but lagging behind Random Forest. This result suggests Gradient Boosting captures more complex patterns than simpler models like Naive Bayes, but it may overfit or require hyperparameter tuning to reach its full potential.
 - Decision Tree (Accuracy: 39.843%): Decision Tree’s low accuracy suggests it may be overfitting to the training data or failing to generalize well. Unlike Random Forest, a single decision tree lacks robustness and may struggle with noisy or complex datasets. Naive Bayes’ poor performance likely stems from its assumption of feature independence, which doesn’t align with real-world data correlations. Decision Tree may have overfitted the training data, lacking the ensemble benefit of Random Forest. Gradient Boosting’s moderate accuracy suggests sensitivity to hyperparameters and noise, which could limit its effectiveness. Random Forest excelled due to its ensemble approach, which mitigates overfitting and handles noisy or high-dimensional data better.

**Conclusion**
 The Random Forest model emerged as the most effective predictor with an impressive accuracy of 88.11%, showcasing its strength in handling complex data relationships and generalizing across different patterns. Its ensemble approach ensures robustness by averaging predictions from multiple decision trees, effectively mitigating overfitting. Gradient Boosting achieved moderate accuracy at 56.24%, indicating it can capture non-linear relationships but may require hyperparameter optimization to reach its full potential. On the other
hand, Decision Tree and Naive Bayes struggled, with accuracies of 39.84% and 31.45%, respectively, highlighting their limitations in managing the dataset’s complexity and nuances. The poor performance of Naive Bayes is likely due to its assumption of feature independence, which does not hold in real-world scenarios where theft patterns are influenced by correlated factors such as time, location, and other contextual variables. Decision Tree’s underperformance can be attributed to overfitting and a lack of ensemble benefits, making it less capable of generalizing. Gradient Boosting’s moderate results suggest sensitivity to noisy data and the need for careful tuning, while Random Forest excelled by leveraging its ensemble method to reduce errors and improve reliability.

** References**

[1] S. Zidi, A. Mihoub, S. Mian Qaisar, M. Krichen, and Q. Abu Al-Haija, “Theft detection dataset for benchmarking and machine learning based classification in a smart grid environment,” Journal of King Saud University- Computer and Information Sciences, vol. 35, no. 1, pp. 13–25, 2023.
[2] H. P. Josyula, K. Patel, A. Bhanushali, Sunil, R. Landge, and S. Mittal, “A review on data visualization for exploratory data analysis,” IEEE, vol. 38, pp. 487–494, 09 2023.
[3] T. P. Service. (2023/ 2024) Bicycle thefts open data. [Online]. Available: https://data.torontopolice.on.ca/datasets/a89d10d5e28444ceb0c8d1d4c0ee39cc0/explore?showTable=true