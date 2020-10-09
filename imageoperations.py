from PIL import Image

def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open("/Users/marlonaleman/Desktop/CS110/Projects/project2/copy.png") 
    imageWidth, imageHeight = inputImage.size
    copyImage(inputImage, imageWidth, imageHeight)   

    print (imageHeight)


    print("Welcome to ImageProcessingX:")
    print("1. Flip the image vertically")
    print("2. Flip the image horizontally")
    print("3. Lighten the image")
    print("4. Darken the image")
    print("5. Scroll the image horizontally")
    print("6. Scroll the image vertically")
    print("7. Grayscale the image")
    print("8. Rotate the image 90 degrees")
    print("9. Swap the corners of an image")

    user_choice = int(input("Choose a number for the action you would like to do to the image:"))    

    if  user_choice == 1:
        flipVertical(inputImage, imageWidth, imageHeight)
    elif user_choice == 2:
        flipHorizontal(inputImage, imageWidth, imageHeight)
    elif user_choice == 3:
        lightenImage(inputImage, imageWidth, imageHeight)
    elif user_choice == 4:
        darkenImage(inputImage, imageWidth, imageHeight)
    elif user_choice == 5:
        numpixels = int(input("How many pixels would you like to scroll?:"))
        scrollHorizontal(inputImage, imageWidth, imageHeight, numpixels)
    elif user_choice == 6:
        numpixels = int(input("How many pixels would you like to scroll?:"))
        scrollVertical(inputImage, imageWidth, imageHeight, numpixels)
    elif user_choice == 7:
        makeGreyscale(inputImage, imageWidth, imageHeight)
    elif user_choice == 8:
        rotate(inputImage, imageWidth, imageHeight)
    elif user_choice == 9:
        swapCorner(inputImage, imageWidth, imageHeight)

    else:
        user_choice = int(input("ERROR. INVALID RESPONSE. Please enter a number 1-4:"))

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/copy.png")

#Flips the image Vertically
def flipVertical(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            newj = imageHeight - 1 - j
            copyImageOutput.putpixel((i, newj), pixelColors)    


    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/flipvertical.png")

#Flips the image Horizontally
def flipHorizontal(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            newXloc = imageWidth - 1 - i
            copyImageOutput.putpixel((newXloc, j), pixelColors)
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/fliphorizontal.png")

#Darkens the image
def darkenImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            amount = 0.25
            pixelColors = inputImage.getpixel((i,j))
            red = pixelColors[0]
            green = pixelColors[1]
            blue = pixelColors[2]
            newRed = int((1 - amount) * red)
            newGreen = int((1 - amount) * green)
            newBlue = int((1 - amount) * blue)
            copyImageOutput.putpixel((i, j), (newRed, newGreen, newBlue))
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/darkenImage.png")

#Lightens the image
def lightenImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            amount = 0.75
            pixelColors = inputImage.getpixel((i,j))
            red = pixelColors[0]
            green = pixelColors[1]
            blue = pixelColors[2]
            newRed = (1 - amount) * red + amount * 255
            newRed = int(newRed)
            newGreen = (1 - amount) * green + amount * 255
            newGreen = int(newGreen)
            newBlue = (1 - amount) * blue + amount * 255
            newBlue = int(newBlue)
            copyImageOutput.putpixel((i,j), (newRed, newGreen, newBlue))
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/lightenImage.png")

#Scrolls the image horizonatally (moves the x values to new positions)
def scrollHorizontal(inputImage, imageWidth, imageHeight, numpixels):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(numpixels, imageWidth):
        for j in range(0, imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            newplaceB = i - numpixels 
            copyImageOutput.putpixel((newplaceB, j), pixelColors)
    difference = imageWidth - numpixels
    for i in range(0, difference):
        for j in range(0, imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            newplaceA = i + numpixels - 1
            copyImageOutput.putpixel((newplaceA, j), pixelColors)
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/scrollHorizontal.png")

#Scrolls the image vertically (moves the y values to new positions)
def scrollVertical(inputImage, imageWidth, imageHeight, numpixels):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(0, imageWidth):
    	for j in range(numpixels, imageHeight):
    		pixelColors = inputImage.getpixel((i,j))
    		newYloc = j - numpixels
    		copyImageOutput.putpixel((i, newYloc), pixelColors)
    difference = imageHeight - numpixels
    for i in range(0, imageWidth):
    	for j in range(0, difference):
    		pixelColors = inputImage.getpixel((i,j))
    		newYloc = j + numpixels
    		print(newYloc)
    		copyImageOutput.putpixel((i, newYloc), pixelColors)

    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/ScrollVertical.png")


#Makes the image grey
def makeGreyscale(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i,j))
            red = pixelColors[0] 
            green = pixelColors[1] 
            blue = pixelColors[2] 
            newRed = int(red * 0.30)
            newGreen = int(green * 0.69)
            newBlue = int(blue * 0.11)
            copyImageOutput.putpixel((i,j), (newRed,newGreen,newBlue))
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/Greyscale.png")

#Rotates the image by 90 degrees
def rotate(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageHeight):
        for j in range(imageWidth):
        	New_Column = i
        	New_row = j
        	pixelColors = inputImage.getpixel((i,j))
        	copyImageOutput.putpixel((New_Column, New_row), pixelColors)
    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/rotate.png")

#Swaps the four quadrants of an image
def swapCorner(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    rangeWidth = int(imageWidth / 2)
    rangeHeight = int(imageHeight / 2)

    for i in range(rangeWidth, imageWidth):
    	for j in range(rangeHeight, imageHeight):
    		pixelColors = inputImage.getpixel((i,j))
    		newWidth = i - rangeWidth
    		newHeight = j - rangeHeight
    		copyImageOutput.putpixel((newWidth, newHeight), pixelColors)
    for i in range(rangeWidth, imageWidth):
    	for j in range(0, rangeHeight):
    		pixelColors = inputImage.getpixel((i,j))
    		newWidth = i - rangeWidth
    		newHeight = j + rangeHeight
    		copyImageOutput.putpixel((newWidth, newHeight), pixelColors)
    for i in range(0, rangeWidth):
    	for j in range(rangeHeight, imageHeight):
    		pixelColors = inputImage.getpixel((i,j))
    		newWidth = i + rangeWidth 
    		newHeight = j - rangeHeight
    		copyImageOutput.putpixel((newWidth, newHeight), pixelColors)
    for i in range(0, rangeWidth):
    	for j in range(0, rangeHeight):
    		pixelColors = inputImage.getpixel((i,j))
    		newWidth = i + rangeWidth
    		newHeight = j + rangeHeight
    		copyImageOutput.putpixel((newWidth, newHeight), pixelColors)

    copyImageOutput.save("/Users/marlonaleman/Desktop/CS110/Projects/project2/SwapCorners.png")


main()