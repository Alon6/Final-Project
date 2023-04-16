# Final-Project
## התקדמות בפרוייקט
### דצמבר:
הצגנו, ותיקנו את הגדרת הפרויקט.
קראנו באופן כללי על הנושא של machine learning. למדנו מה זה machine learning, קראנו על טכניקות של machine learning ובפרט deep learning. למדנו באופן כללי איך רשת נוירונים עובדת, איך מאמנים ומשתמשים במודל של deep learning וגם ראינו שימושים של machine learning במגוון תחומים. 
### ינואר:
בחרנו במודל הimage captioning של BLIP שנמצא בספרייה LAVIS (LAVIS זאת ספרייה שיש מודלים של למידת מכונה המבצעים מספר משימות מתחומים של ראייה ממוחשבת ועיבוד שפות טבעיות, ובפרט אחד המודלים שנמצאים בה הוא מודל הBLIP שעושה image captioning) להיות המודל שעליו נעשה finetuning עבור אוסף התמונות של הספרייה הלאומית.
הורדנו את המודל ועשינו לו evaluate על מספר תמונות מהאוסף תמונות.
#### דוגמאות לevaluation של המודל:

<img src="https://user-images.githubusercontent.com/99743983/218708420-c4396c1d-bc9d-4449-8ffa-1712d8b11165.jpg" width="200"/>

הפלט של המודל: 'a black and white photo of a brick building'

<img src="https://user-images.githubusercontent.com/99743983/218711812-d095a174-5500-4c80-bd29-274244c5d674.png" width="200"/>

הפלט של המודל: 'a couple of men standing next to each other'

<img src="https://user-images.githubusercontent.com/99743983/218713866-65f9717f-c6f0-4fde-95d2-0fb08fe360ef.png" width="300"/>

הפלט של המודל: 'a black and white photo of two boys wearing hats'
### פברואר:
תיאמנו וקיימנו פגישה עם נציג מהספרייה הלאומית שהסביר לנו על אוסף התמונות של הספרייה הלאומית שנשתמש בהן בביצוע הfinetuning, ובפרט הוא הסביר כיצד להשיג את התמונות ואת התיאור שלהן תוך שימוש בAPI של הספרייה הלאומית, וגם איך לזהות ולהוציא את התיאור של התמונות עבור הfinetuning.
### מרץ:
יצרנו תכנית שמשתמשת בAPI של הספרייה הלאומית על מנת לקבל את הmetadata של התמונות הרלוונטיות (בפרט קישור לתמונות עצמן), ולאחר מכן עושה evaluate לאותן תמונות (בשלבים הבאים נשתמש בתכנית זו בשביל להביא את התמונות שבעזרתן נעשה finetune למודל).
### אפריל:
ביצענו הכנה ל-fine-tuning: לאחר קבלת התמונות מה-API של הספרייה הלאומית, עשינו extraction ל-label של כל תמונה מה-metadata - זהו בעצם ה-label האמיתי של התמונה (אנחנו מצפים שה-label הזה יהיה הפלט של מודל ה-BLIP). כמו כן, תירגמנו את כל ה-labels שאינם באנגלית להיות באנגלית. לאחר מכן, הצגנו, עבור כל תמונה, את הפלט שלה ממודל ה-BLIP, לעומת ה-label האמיתי (שעשינו לו extraction) שלה.
