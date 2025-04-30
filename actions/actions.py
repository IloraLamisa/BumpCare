from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import sqlite3

# Path to the database
# DATABASE_PATH = "/Client/appointments.db"

class ActionAskBreakfast(Action):
    def name(self) -> Text:
        return "action_ask_breakfast"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Log the slot value for debugging
        # user_message = tracker.latest_message.get('text').lower()
        trimester = tracker.get_slot("trimester")
        print(f"DEBUG 1: Trimester slot value: {trimester}")
        # print(f"DEBUG 2: user_message : {user_message}")
        
        # Check if the trimester slot is set and valid
        if trimester == "first":
            dispatcher.utter_message(response="utter_first_trimester_breakfast")
        elif trimester == "second":
            dispatcher.utter_message(response="utter_second_trimester_breakfast")
        elif trimester == "third":
            dispatcher.utter_message(response="utter_third_trimester_breakfast")
        else:
            dispatcher.utter_message(
                text="I'm sorry, I didn't catch your trimester. Can you specify if you're in your (first | second | third)?"
            )

        return []

class ActionAskLunch(Action):
    def name(self) -> Text:
        return "action_ask_lunch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Initialize lunch variable with a default message
        lunch = "I couldn't determine your trimester. Can you clarify?"

        # Retrieve the trimester slot value
        trimester = tracker.get_slot("trimester")
        
        # Log the received trimester value for debugging
        print(f"Received trimester value: {trimester}")

        # Check if trimester is valid
        if not any([trimester == "first", trimester == "second", trimester == "third"]):
            dispatcher.utter_message(text="I'm sorry, I didn't catch your trimester. Can you specify if you're in your (first | second | third)?")
            return []  # Exit early if the input is invalid

        # Proceed with valid trimester responses
        if trimester == "first":
            lunch = "For lunch, you can try: Grilled chicken salad with leafy greens."
            dispatcher.utter_message(response="utter_first_trimester_lunch")
        elif trimester == "second":
            lunch = "For lunch, consider: Quinoa salad with chickpeas."
            dispatcher.utter_message(response="utter_second_trimester_lunch")
        elif trimester == "third":
            lunch = "For lunch, how about: Lentil soup?"
            dispatcher.utter_message(response="utter_third_trimester_lunch")

        # Send response to the user
        dispatcher.utter_message(text=lunch)
        return []

class ActionAskDinner(Action):
    def name(self) -> Text:
        return "action_ask_dinner"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
              # Retrieve the trimester slot value
        trimester = tracker.get_slot("trimester")
        
        # Check if trimester is valid
        if not any([trimester == "first", trimester == "second", trimester == "third"]):
            dispatcher.utter_message(text="I'm sorry, I didn't catch your trimester. Can you specify if you're in your (first|second|third)?")
            return []  # Exit early if the input is invalid
        
        trimester = tracker.get_slot("trimester")
        if trimester == "first":
            dispatcher.utter_message(response="utter_first_trimester_dinner")
        elif trimester == "second":
            dispatcher.utter_message(response="utter_second_trimester_dinner")
        elif trimester == "third":
            dispatcher.utter_message(response="utter_third_trimester_dinner")

        return []  # Ensure slot is set

class ActionProvideMealPlan(Action):
    def name(self):
        return "action_provide_meal_plan"

    def run(self, dispatcher, tracker, domain):
        # Get slot value
        trimester = tracker.get_slot("trimester")
        print(f"Debug: trimester slot value = {trimester}")  # Debugging line

        # Determine meal plan based on trimester
        if trimester == "first":
            meal_plan = (
        "Here's a recommended meal plan for the first trimester:\n\n"
        "Key Nutritional Needs:\n"
        "- **Folate**: Essential for early neural tube development.\n"
        "- **Iron**: Prevents anemia, which is common in early pregnancy.\n"
        "- **Protein**: Supports tissue growth, including the placenta.\n\n"
        
        "Breakfast:\n"
        "- **Option 1**: Oatmeal with ground flaxseeds, a tablespoon of almond butter, and sliced banana.\n"
        "  - Flaxseeds provide omega-3s; bananas offer potassium.\n"
        "- **Option 2**: Whole grain toast with avocado and a poached egg.\n"
        "  - Provides protein and healthy fats.\n\n"
        
        "Lunch:\n"
        "- **Option 1**: Grilled chicken or tofu salad with leafy greens (spinach, kale), cucumber, and cherry tomatoes. "
        "Top with a vinaigrette dressing.\n"
        "  - Leafy greens provide folate; chicken or tofu gives you protein.\n"
        "- **Option 2**: Quinoa salad with chickpeas, mixed greens, olive oil, and lemon.\n"
        "  - Chickpeas and quinoa offer plant-based protein and fiber.\n\n"
        
        "Snacks:\n"
        "- **Option 1**: A small handful of almonds and dried apricots (rich in iron).\n"
        "- **Option 2**: Greek yogurt with fresh berries (calcium and antioxidants).\n"
        "- **Option 3**: Carrot sticks with hummus (protein, fiber).\n\n"
        
        "Dinner:\n"
        "- **Option 1**: Grilled salmon (or another omega-3 rich fish) with roasted sweet potatoes and steamed broccoli.\n"
        "  - Omega-3s for brain development and sweet potatoes for vitamin A.\n"
        "- **Option 2**: Lentil stew with tomatoes, onions, and spinach served with whole grain bread.\n"
        "  - Lentils provide iron and fiber; spinach provides folate.\n\n"
        
        "<br><strong>Additional Considerations for Week 1-12:</strong>\n"
        "- **Folic acid**: 400–800 mcg daily through supplements or fortified foods.\n"
        "- **Iron-rich foods**: Include lean meats, lentils, fortified cereals, and spinach.\n"
        "- **Hydration**: Drink water consistently to combat morning sickness."
    )
        elif trimester == "second":
            meal_plan = (
        "Here's a recommended meal plan for the second trimester:\n\n"
        "Key Nutritional Needs:\n"
        "- **Calcium**: Essential for the baby's bone development.\n"
        "- **Omega-3s**: Supports brain and eye development.\n"
        "- **Iron**: Necessary due to increased blood volume.\n\n"
        
        "Breakfast:\n"
        "- **Option 1**: Scrambled eggs with spinach, whole grain toast, and a side of orange slices.\n"
        "  - Spinach provides folate; eggs give protein.\n"
        "- **Option 2**: Smoothie with kale, banana, protein powder, chia seeds, and almond milk.\n"
        "  - Chia seeds provide omega-3s; bananas offer potassium.\n\n"
        
        "Lunch:\n"
        "- **Option 1**: Turkey or chicken wrap with whole wheat tortilla, avocado, lettuce, and tomato.\n"
        "  - Avocado provides healthy fats; turkey or chicken offers protein.\n"
        "- **Option 2**: Quinoa bowl with black beans, roasted vegetables (bell peppers, zucchini), and a sprinkle of feta cheese.\n"
        "  - Beans are an excellent source of plant protein; quinoa is a complete protein.\n\n"
        
        "Snacks:\n"
        "- **Option 1**: A handful of mixed nuts and a small apple.\n"
        "  - Nuts are a good source of protein and healthy fats.\n"
        "- **Option 2**: A boiled egg with carrot sticks.\n"
        "- **Option 3**: Cottage cheese with pineapple.\n"
        "  - Calcium and protein from cottage cheese; vitamin C from pineapple.\n\n"
        
        "Dinner:\n"
        "- **Option 1**: Baked salmon with a quinoa salad (with cucumber, tomatoes, and olive oil).\n"
        "  - Salmon provides omega-3s; quinoa offers fiber and protein.\n"
        "- **Option 2**: Stir-fried tofu with vegetables (broccoli, bell peppers, carrots) and brown rice.\n"
        "  - Tofu is a plant-based protein; veggies offer vitamins; brown rice provides fiber.\n\n"
        
        "<br><strong>Additional Considerations for Week 13-26:</strong>\n"
        "- **Calcium**: Aim for 1,000 mg per day (dairy products, fortified plant milk, leafy greens).\n"
        "- **Iron**: Consider iron supplements if recommended by your doctor (iron-rich foods include lean meats, fortified cereals, beans).\n"
        "- **Magnesium**: Include nuts, seeds, and whole grains to support muscle relaxation and reduce leg cramps."
    )
        elif trimester == "third":
            meal_plan = (
        "Here's a recommended meal plan for the third trimester:\n\n"
        "Key Nutritional Needs:\n"
        "- **Protein**: Essential for fetal growth and development.\n"
        "- **Calcium**: Crucial for the baby’s bone development.\n"
        "- **Fiber**: Helps prevent constipation, which is common during this stage.\n"
        "- **Omega-3s**: Vital for the baby’s brain development.\n\n"
        
        "Breakfast:\n"
        "- **Option 1**: Whole grain waffles with peanut butter and sliced strawberries.\n"
        "  - Whole grains provide fiber; peanut butter gives protein.\n"
        "- **Option 2**: Greek yogurt parfait with granola, chia seeds, and blueberries.\n"
        "  - Greek yogurt is high in calcium and protein; chia seeds provide omega-3s.\n\n"
        
        "Lunch:\n"
        "- **Option 1**: Grilled chicken or chickpea and avocado wrap with spinach and whole grain tortilla.\n"
        "  - Avocado provides healthy fats; chicken or chickpeas give protein.\n"
        "- **Option 2**: Whole wheat pasta with a tomato and spinach sauce, topped with parmesan cheese.\n"
        "  - Whole wheat pasta offers fiber; spinach provides folate and calcium.\n\n"
        
        "Snacks:\n"
        "- **Option 1**: Rice cakes with almond butter and sliced banana.\n"
        "- **Option 2**: Veggie sticks (carrot, cucumber, celery) with guacamole.\n"
        "- **Option 3**: Apple slices with cheddar cheese.\n"
        "  - Cheese provides calcium; apples offer fiber.\n\n"
        
        "Dinner:\n"
        "- **Option 1**: Grilled chicken or salmon with roasted Brussels sprouts and quinoa.\n"
        "  - Chicken or salmon provides protein; quinoa and Brussels sprouts are high in fiber and folate.\n"
        "- **Option 2**: Veggie-loaded stir-fry with tofu, carrots, broccoli, bell peppers, and brown rice.\n"
        "  - Tofu provides protein; veggies offer vitamins and fiber.\n\n"
        
        "Additional Considerations for Week 27-40:\n"
        "- **Protein**: Include a good amount of protein at every meal to support muscle and tissue repair.\n"
        "- **Calcium**: Aim for 1,000–1,300 mg per day from dairy, leafy greens, or fortified foods.\n"
        "- **Fiber**: Increase fiber intake with whole grains, fruits, and vegetables to improve digestion.\n\n"
        
        "<br><strong>Additional Guidelines:</strong>\n"
        "- **Hydration**: Drink 8-10 cups of water daily, more if you are physically active.\n"
        "- **Prenatal vitamins**: Continue taking prenatal vitamins with folic acid, iron, and calcium."
    )
        else:
            # Log issue with slot value
            print("Debug: Slot value for 'trimester' is invalid or not set.")
            meal_plan = "I couldn't determine your trimester for meal plan. plz Clarify like as (first|second|third)"

        # Send response to the user
        dispatcher.utter_message(text=meal_plan)
        return []

# class ActionVoiceInput(Action):
#     def name(self) -> Text:
#         return "action_voice_input"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
#         try:
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 print("Speak Now!")
#                 audio = r.listen(source, timeout=5)  # Set a timeout for recording
#                 text = r.recognize_google(audio)
#                 print(f"You said: {text}")
#                 return [SlotSet("user_input", text)]

#         except sr.UnknownValueError:
#             dispatcher.utter_message(text="I couldn't understand that. Please try again.")
#             return []
#         except sr.RequestError as e:
#             dispatcher.utter_message(text=f"Could not request results from Google Speech Recognition service; {e}")
#             return []
#         except Exception as e:
#             dispatcher.utter_message(text=f"An error occurred: {e}")
#             return [] 

class ActionProvideWeekGroup(Action):
    def name(self):
        return "action_provide_week_group"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        week_group = tracker.get_slot("week_group")
        age_group = tracker.get_slot("age_group")
        print("Latest message from week_group:", tracker.latest_message.get("text"))
        print("get_slot from week group:", week_group)

        if week_group == "1-13":
            dispatcher.utter_message(response="utter_Weeks_1_13_baby_development")
        elif week_group == "14-26":
            dispatcher.utter_message(response="utter_Weeks_14_26_baby_development")
        elif week_group in ["27+", "27-40"]:
            dispatcher.utter_message(response="utter_Weeks_27_40_baby_development")
        elif age_group == "18-30":
            dispatcher.utter_message(response="utter_18_30_exercise")
        elif age_group == "31-39":
            dispatcher.utter_message(response="utter_31_39_exercise")
        elif age_group == "40+":
            dispatcher.utter_message(response="utter_40_plus_exercise")
        else:
            dispatcher.utter_message(
                text="Please specify weeks like this (e.g., 1-13, 14-26, or 27-40)."
            )
        return []

# this function not working properly  
class ActionProvideAgeGroupInfo(Action):
    def name(self):
        return "action_provide_age_group_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        age_group = tracker.get_slot("age_group")
        print("Latest message age_group:", tracker.latest_message.get("text"))
        print("get_slot age_group:", age_group)

        if age_group == "18-30":
            dispatcher.utter_message(response="utter_18_30_exercise")
        elif age_group == "31-39":
            dispatcher.utter_message(response="utter_31_39_exercise")
        elif age_group == "40+":
            dispatcher.utter_message(response="utter_40_plus_exercise")
        else:
            dispatcher.utter_message(text="Sorry, I don't have specific exercise tips for that age group.")
        return []

class ActionFindGynaecologistByDay(Action):
    def name(self) -> str:
        return "action_find_gynaecologist_by_day"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        appointment_day = tracker.latest_message.get("text")

        if appointment_day:
            appointment_day = appointment_day.lower() 

            if "saturday" in appointment_day or "sunday" in appointment_day:
                dispatcher.utter_message(template="utter_gynaecologist_Satarday_Sunday")
            elif "monday" in appointment_day or "tuesday" in appointment_day:
                dispatcher.utter_message(template="utter_gynaecologist_Monday_tuesday")
            elif "wednesday" in appointment_day or "thursday" in appointment_day:
                dispatcher.utter_message(template="utter_gynaecologist_wednesday_thursday")
            elif "friday" in appointment_day:
                dispatcher.utter_message(template="utter_gynaecologist_Friday")
            else:
                dispatcher.utter_message(text="Please enter your appointment valid day. (e.g., Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, today, tomorrow).")
        else:
            dispatcher.utter_message(text="Please specify the appointment day.")

        return []



# Action to save an appointment to the database
# class ActionSaveAppointment(Action):
#     def name(self) -> Text:
#         return "action_save_appointment"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract details from user's input
#         user_name = tracker.get_slot("user_name")
#         doctor_name = tracker.get_slot("doctor_name")
#         appointment_date = tracker.get_slot("appointment_date")
#         reason = tracker.get_slot("reason")

#         # Ensure all slots are filled
#         if not (user_name and doctor_name and appointment_date and reason):
#             dispatcher.utter_message(text="Please provide your name, doctor name, appointment date, and reason.")
#             return []

#         # Insert appointment into the database
#         try:
#             conn = sqlite3.connect(DATABASE_PATH)
#             cursor = conn.cursor()

#             cursor.execute("""
#                 INSERT INTO appointments (user_name, doctor_name, appointment_date, reason)
#                 VALUES (?, ?, ?, ?)
#             """, (user_name, doctor_name, appointment_date, reason))

#             conn.commit()
#             conn.close()

#             dispatcher.utter_message(text="Your appointment has been saved successfully!")
#         except Exception as e:
#             dispatcher.utter_message(text=f"An error occurred while saving the appointment: {str(e)}")

#         return []


# Action to retrieve appointments from the database
# class ActionRetrieveAppointments(Action):
#     def name(self) -> Text:
#         return "action_retrieve_appointments"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_name = tracker.get_slot("user_name")  # Get the user's name

#         if not user_name:
#             dispatcher.utter_message(text="Please provide your name to retrieve your appointments.")
#             return []

#         try:
#             conn = sqlite3.connect(DATABASE_PATH)
#             cursor = conn.cursor()

#             # Retrieve appointments for the specific user
#             cursor.execute("""
#                 SELECT doctor_name, appointment_date, reason FROM appointments
#                 WHERE user_name = ?
#             """, (user_name,))
#             rows = cursor.fetchall()
#             conn.close()

#             if rows:
#                 message = "Here is your appointment details:\n"
#                 for row in rows:
#                     message += f"- Doctor: {row[0]}, Date: {row[1]}, Reason: {row[2]}\n"
#             else:
#                 message = "You have no saved appointments."

#             dispatcher.utter_message(text=message)
#         except Exception as e:
#             dispatcher.utter_message(text=f"An error occurred while retrieving appointments: {str(e)}")

#         return []
#     def name(self) -> Text:
#         return "action_retrieve_appointments"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_name = tracker.get_slot("user_name")  # Retrieve user's name

#         try:
#             conn = sqlite3.connect(DATABASE_PATH)
#             cursor = conn.cursor()

#             # Retrieve appointments for the specific user
#             cursor.execute("""
#                 SELECT appointment_date, doctor_name, reason FROM appointments
#                 WHERE user_name = ?
#             """, (user_name,))
#             rows = cursor.fetchall()
#             conn.close()

#             if rows:
#                 message = "Here are your appointments:\n"
#                 for row in rows:
#                     message += f"- Date: {row[0]}, Doctor: {row[1]}, Reason: {row[2]}\n"
#             else:
#                 message = "You have no saved appointments."

#             dispatcher.utter_message(text=message)
#         except Exception as e:
#             dispatcher.utter_message(text=f"An error occurred while retrieving appointments: {str(e)}")

#         return []

