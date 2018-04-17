# challanges

As we understand the algorithm , if we see our [dataset](./gpa.csv) we may find some similarity which may affect our predictions, i.e for some similar gpa's there are different sat scores or vice-versa.<br>

    for e.g.
    
        GPA       SAT SCORE
        4.0       1220
        2.8       1220
        
        etc.
 Like that there are some few cases, so what happens now and how does algorithms deals with it ? that is the question .<br>
 To answer that lets see the actual regression algorithm step by step.
 
 <b>step 1:</b>To observe our goal
 
 ![alt_tag](https://github.com/vshantam/Sat_prediction/blob/master/Image/O752N.png)
 
 Clearly you can see that we have our cost function with some parameters to minimize the function with minimum error using gradient descent algorithm because it is necessary to produce much efficient results with less predictive errors.
 
 <b>step 2:</b> How do we minimize and why ?
 
 ![alt_tag](https://github.com/vshantam/Sat_prediction/blob/master/Image/grad.png)
 
 The first step we choose towards the minimization problems is the learning rate <b>alpha</b>.The bigger the learning rate the faster the algorithm learns but with less accuracy and efficient but if the learning rate is much small the algorithm learns slowly but more accurately which causes less predictive errors.<br>
 <b> Gradient descent </b> :it is the actual math behind the algorithm .<br>
 ![alt_tag](https://github.com/vshantam/Sat_prediction/blob/master/Image/89edQ.png)
 
 What it is actually doing is that it is updating the cost fuction  with its hypothetical perameter that is <b> theta_1 </b> and <b> Theta_2</b>.The both parameters plays a vital role in predicting the results because these  parameters are the main components in the hypothesis above.so, it is very important to train and aquire the hypothetical parameters accurately.<br>
 Once the parameters have been processed it will be fixed and there will be no more further changes in the parameter.
 
 To make you understand better let me show you results from my implemetation which you can check out from [here](https://github.com/vshantam/Machine-learning)
 
 ![alt_tag](https://github.com/vshantam/Machine-learning/blob/master/images/Capture2.PNG)
  As you can see in the image the how the results improves over the iteration and the final results of <b> Theta_1</b> and <b> Theta_2</b><br>
  Now that our hypothesis is ready we can predict based on the parameters that we pass (in this case Theta_1 and Theta_2).
  if we want to predict something we just need to pass the arguments to predicts the result.<br>
  ## Note
  
  <b> It is important to understand the hypothetical parameters are fixed over the entire process , it does not matters how may times you enters the same elements to predict, it will predict the same because we are using the same Theta_1 and Theta_2 over and over again.</b>
  
  ### Solution
  we you observe our dataset there is only one feature and one labels , to overcome our challange  it is recommended that we use more numbers of feature to our algorithms which will give the better results because the learning is based on the different parameter that we use as a features to understand the circumstances.
 
