import cv2
import numpy as np

def enhance_image(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)
    
    
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    
    if avg_brightness > 170:  
        
        clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))
        alpha = 0.85  
        beta = -15    
    elif avg_brightness < 80:  
        
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
        alpha = 1.15  
        beta = 10     
    else:  
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        alpha = 1.05
        beta = 0      
    
    
    enhanced_l = clahe.apply(l)
    
    
    enhanced_lab = cv2.merge([enhanced_l, a, b])
    
    
    enhanced = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    
    enhanced = cv2.convertScaleAbs(enhanced, alpha=alpha, beta=beta)
    
    print(f"Image brightness: {avg_brightness:.1f}")
    print(f"Applied adjustments - Contrast: {alpha:.2f}, Brightness: {beta}")
    
    return enhanced
    

def process_image(file_path):
    
    if not file_path:
        print("No file path provided!")
        return
    
    
    image = cv2.imread(file_path)
    if image is None:
        print("Error loading image!")
        return
    
    
    enhanced = enhance_image(image)
    
    
    output_path = file_path.rsplit('.', 1)[0] + '_enhanced.' + file_path.rsplit('.', 1)[1]
    cv2.imwrite(output_path, enhanced)
    print(f"Enhanced image saved as: {output_path}")

def main():
    while True:
        
        file_path = input("\nEnter the path to your image (or 'q' to quit): ")
        
        
        if file_path.lower() == 'q':
            print("Goodbye!")
            break
        
        
        process_image(file_path)

if __name__ == "__main__":
    main()
