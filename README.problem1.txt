COMPSCI 260 - Problem Set 6, Problem 1
Due: Wed 23 November 2022, 5pm

Name: Henry Gussis
NetID: hsg11

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/bs704_probability6.html

My solutions and comments for this problem are below.
-----------------------------------------------------
A.
    This table summarizes the amount of positive and negative tests given the disease prevalence of 1/40000 and test accuracy of 0.997
                Diseased        Not Diseased        Total
    + Test        0.997            119.997          120.994
    - Test        0.003            39,879.003       39,879.006
    Total          1               39,999           40,000
    P(A) = The unconditional probability that Murray has the disease (prevalence) = 1/40000 = 0.000025
    p(B) = The unconditional probability that Murray has a positive test = (120.994/40000) = 0.00302485
    P(B|A) = Probability that Murray has a positive test given he has the disease = 0.997
    We want to know P(A|B): the probability that Murray has the disease given he has a positive test
    Bayes's Theorem: P(A|B) = P(B|A)*P(A)/P(B)
    Therefore: P(A|B) = (0.997*0.000025)/0.00302485 = 0.00824

    The probability that Murray has the disease given he had a positive test is 0.00824

    Therefore, it is still very unlikely that Murray has the disease

B. I would tell Murray that because of the prevalence rate being substantially lower than the false positive rate,
   it is highly unlikely that he has the disease despite his positive test. In order to observe a more reasonable
   false discovery rate, the test would have to diagnose fewer false positives or more true positives to increase
   the ratio of (True + / [True + plus False +]). This would increase
   the accuracy of the test, thus increasing the conditional probability that a patient has the disease given they
   tested positive for it.

C. If certain environmental factors contributed to this disease, then my conclusion from part A would not hold. This
   is because the conditional probability would change. For example, the Probability would be:
   P(Murray has the disease| He has a positive test AND was exposed to contributing environmental factors).
   This would mean that the original probability found in part A would be less accurate since there are no statistics
   about how these environmental factors affect the probability of developing the disease or having a false +/- test.