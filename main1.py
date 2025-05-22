import cv2
import numpy as np

def enhance_image(image):
    # First analyze brightness
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)
    
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    # Create CLAHE object with parameters based on brightness
    if avg_brightness > 170:  # Too bright
        # Use more aggressive contrast limiting for bright images
        clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
        alpha = 0.85  # Reduce contrast
        beta = -15    # Reduce brightness
    elif avg_brightness < 80:  # Too dark
        # Use less contrast limiting for dark images
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
        alpha = 1.15  # Increase contrast
        beta = 10     # Increase brightness
    else:  # Normal brightness
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        alpha = 1.05  # Very slight contrast boost
        beta = 0      # No brightness change
    
    # Apply CLAHE to L channel
    enhanced_l = clahe.apply(l)
    
    # Merge channels back
    enhanced_lab = cv2.merge([enhanced_l, a, b])
    
    # Convert back to BGR
    enhanced = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    # Apply final adjustments
    enhanced = cv2.convertScaleAbs(enhanced, alpha=alpha, beta=beta)
    
    print(f"Image brightness: {avg_brightness:.1f}")
    print(f"Applied adjustments - Contrast: {alpha:.2f}, Brightness: {beta}")
    
    return enhanced
    
    print(f"Image statistics:")
    print(f"Original - Brightness: {brightness:.1f}, Contrast: {contrast:.1f}")
    print(f"Adjustments - Contrast multiplier: {alpha:.2f}, Brightness change: {beta:.1f}")
    
    return enhanced

def process_image(file_path):
    # Validate file path
    if not file_path:
        print("No file path provided!")
        return
    
    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        print("Error loading image!")
        return
    
    # Enhance the image
    enhanced = enhance_image(image)
    
    # Save the enhanced image
    output_path = file_path.rsplit('.', 1)[0] + '_enhanced.' + file_path.rsplit('.', 1)[1]
    cv2.imwrite(output_path, enhanced)
    print(f"Enhanced image saved as: {output_path}")

def main():
    while True:
        # Get image path from user
        file_path = input("\nEnter the path to your image (or 'q' to quit): ")
        
        # Check if user wants to quit
        if file_path.lower() == 'q':
            print("Goodbye!")
            break
        
        # Process the image
        process_image(file_path)

if __name__ == "__main__":
    main()
