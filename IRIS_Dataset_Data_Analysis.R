# Data Analysis by R Programming on IRIS Dataset
# import
library(psych)

# create file
data = read.csv("/Users/nutan/Desktop/Regression_Assignment/data/iris_data.csv")

head(data)
tail(data)
summary(data)

install.packages("psych")
library(psych)
describe(data)

missing = data[!complete.cases(data)]
plot(data)


data = data[-c(1:36), ]
head(data)
tail(data)

cat("\014")
slice = data[,c("SepalLength","SepalWidth")]
summary(slice)

sd(slice$SepalLength)
sd_SepalLength = sd(slice$SepalLength)

sd_SepalWidth = sd(slice$SepalWidth)

mean_SepalLength =(slice$SepalLength)
mean_SepalWidth =(slice$SepalWidth) 


#Set up a 1x2 plotting area
par(mfrow = c(1, 2))

hist(slice$SepalLength,
     main = "Histogram of SepalLength", 
     xlab = "Sepal Length",   # Corrected x-axis label as a string
     col = "red", 
     breaks =10,
     border = "black")


hist(slice$SepalWidth,
     main = "Histogram of SepalWidth", 
     xlab = "Sepal Width",    # Corrected x-axis label as a string
     col = "blue", 
     breaks =10,
     border = "black")

par(mfrow=c(2,1))

hist(slice$SepalLength,
     breaks = 10,
     main = "Histogram of SepalLength",
     xlab = "SepalLength",
     col = "red",
     border = "black")

hist(slice$SepalWidth,
    breaks = 10,
    main = "Histogram of SepalWidth",
    xlab = "SepalWidth",
    col ="blue",
    border = "black")
    
unique(data$Species)
# Ensure Species is a factor with three levels
data$Species <- factor(data$Species, levels = c("setosa", "versicolor", "virginica"))

# Remove any rows with NA values
data <- na.omit(data)


# Boxplot for Sepal Length grouped by Species
boxplot(SepalLength ~ Species, 
        data = data, 
        main = "Boxplot of Sepal Length by Species", 
        xlab = "Species", 
        ylab = "Sepal Length", 
        col = c("red", "green", "blue"))




# Check the unique species
unique(data$Species)

# Create boxplot to check if all species are plotted
boxplot(SepalLength ~ Species, 
        data = data, 
        main = "Boxplot of Sepal Length by Species", 
        xlab = "Species", 
        ylab = "Sepal Length", 
        col = c("red", "green", "blue"))






data$Species = factor(data$Species, levels = c("setosa", "versicolor", "virginica"))
print(unique(data$Species))

print(table(data$Species))
# Create boxplot
boxplot(SepalLength ~ Species, 
        data = data, 
        main = "Boxplot of Sepal Length by Species", 
        xlab = "Species", 
        ylab = "Sepal Length", 
        col = c("red", "green", "blue"))




# Create a scatter plot of PetalLength vs PetalWidth

svg("/Users/nutan/Desktop/Regression_Assignment/Scatterplot.svg")
plot(data$PetalLength, data$PetalWidth, 
     main = "Scatter Plot of PetalLength vs PetalWidth", 
     xlab = "Petal Length", 
     ylab = "Petal Width", 
     pch = 19,          # Plot character (19 for solid circle)
     col = "blue")      # Color of the points
dev.off()


Box plot of PetalLength grouped by Species
boxplot(PetalLength ~ Species, 
        data = data, 
        main = "Box Plot of Petal Length by Species", 
        xlab = "Species", 
        ylab = "Petal Length", 
        col = c("red", "green", "blue"))
