{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "77753f38-02f3-4d75-a7fb-a7389a92c269",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "y contains previously unseen labels: 17",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\_encode.py:225\u001b[0m, in \u001b[0;36m_encode\u001b[1;34m(values, uniques, check_unknown)\u001b[0m\n\u001b[0;32m    224\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 225\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m _map_to_integer(values, uniques)\n\u001b[0;32m    226\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\_encode.py:165\u001b[0m, in \u001b[0;36m_map_to_integer\u001b[1;34m(values, uniques)\u001b[0m\n\u001b[0;32m    164\u001b[0m table \u001b[38;5;241m=\u001b[39m _nandict({val: i \u001b[38;5;28;01mfor\u001b[39;00m i, val \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(uniques)})\n\u001b[1;32m--> 165\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m np\u001b[38;5;241m.\u001b[39marray([table[v] \u001b[38;5;28;01mfor\u001b[39;00m v \u001b[38;5;129;01min\u001b[39;00m values])\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\_encode.py:159\u001b[0m, in \u001b[0;36m_nandict.__missing__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    158\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mnan_value\n\u001b[1;32m--> 159\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m(key)\n",
      "\u001b[1;31mKeyError\u001b[0m: 17",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 41\u001b[0m\n\u001b[0;32m     35\u001b[0m wheel \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mselectbox(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWheel\u001b[39m\u001b[38;5;124m\"\u001b[39m, categories[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWheel\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[0;32m     37\u001b[0m \u001b[38;5;66;03m# ==========================\u001b[39;00m\n\u001b[0;32m     38\u001b[0m \u001b[38;5;66;03m# 3. Encode Inputs\u001b[39;00m\n\u001b[0;32m     39\u001b[0m \u001b[38;5;66;03m# ==========================\u001b[39;00m\n\u001b[0;32m     40\u001b[0m features_cat \u001b[38;5;241m=\u001b[39m {\n\u001b[1;32m---> 41\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mManufacturer\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mManufacturer\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([manufacturer])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     42\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mModel\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mModel\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([model_name])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     43\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCategory\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCategory\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([category])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     44\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFuel type\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFuel type\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([fuel_type])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     45\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mColor\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mColor\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([color])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     46\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLeather interior\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLeather interior\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([leather_interior])[\u001b[38;5;241m0\u001b[39m],\n\u001b[0;32m     47\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWheel\u001b[39m\u001b[38;5;124m\"\u001b[39m: LabelEncoders[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWheel\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtransform([wheel])[\u001b[38;5;241m0\u001b[39m]\n\u001b[0;32m     48\u001b[0m }\n\u001b[0;32m     50\u001b[0m \u001b[38;5;66;03m# Final feature array\u001b[39;00m\n\u001b[0;32m     51\u001b[0m input_data \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([[levy, engine_vol, mileage, cylinders, airbags, prod_year,\n\u001b[0;32m     52\u001b[0m                         features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mManufacturer\u001b[39m\u001b[38;5;124m\"\u001b[39m], features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mModel\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m     53\u001b[0m                         features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCategory\u001b[39m\u001b[38;5;124m\"\u001b[39m], features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFuel type\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m     54\u001b[0m                         features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mColor\u001b[39m\u001b[38;5;124m\"\u001b[39m], features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLeather interior\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m     55\u001b[0m                         features_cat[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWheel\u001b[39m\u001b[38;5;124m\"\u001b[39m]]])\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\sklearn\\preprocessing\\_label.py:137\u001b[0m, in \u001b[0;36mLabelEncoder.transform\u001b[1;34m(self, y)\u001b[0m\n\u001b[0;32m    134\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m _num_samples(y) \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m    135\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m np\u001b[38;5;241m.\u001b[39marray([])\n\u001b[1;32m--> 137\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _encode(y, uniques\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclasses_)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\sklearn\\utils\\_encode.py:227\u001b[0m, in \u001b[0;36m_encode\u001b[1;34m(values, uniques, check_unknown)\u001b[0m\n\u001b[0;32m    225\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m _map_to_integer(values, uniques)\n\u001b[0;32m    226\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m--> 227\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my contains previously unseen labels: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28mstr\u001b[39m(e)\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    228\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    229\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m check_unknown:\n",
      "\u001b[1;31mValueError\u001b[0m: y contains previously unseen labels: 17"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# ==========================\n",
    "# 1. Load Model & Encoders\n",
    "# ==========================\n",
    "with open(\"random_forest_model.pkl\", \"rb\") as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "with open(\"label_encoders.pkl\", \"rb\") as file:\n",
    "    LabelEncoders = pickle.load(file)\n",
    "\n",
    "with open(\"categories.pkl\", \"rb\") as file:\n",
    "    categories = pickle.load(file)\n",
    "\n",
    "st.title(\"🚗 Car Price Prediction App\")\n",
    "\n",
    "# ==========================\n",
    "# 2. Collect Inputs\n",
    "# ==========================\n",
    "levy = st.number_input(\"Levy\", value=1000.0, step=100.0)\n",
    "engine_vol = st.number_input(\"Engine Volume (liters)\", value=2.0, step=0.1)\n",
    "mileage = st.number_input(\"Mileage (km)\", value=50000.0, step=1000.0)\n",
    "cylinders = st.number_input(\"Cylinders\", value=4, step=1)\n",
    "airbags = st.number_input(\"Airbags\", value=2, step=1)\n",
    "prod_year = st.number_input(\"Production Year\", value=2015, step=1)\n",
    "\n",
    "manufacturer = st.selectbox(\"Manufacturer\", categories[\"Manufacturer\"])\n",
    "model_name = st.selectbox(\"Model\", categories[\"Model\"])\n",
    "category = st.selectbox(\"Category\", categories[\"Category\"])\n",
    "fuel_type = st.selectbox(\"Fuel Type\", categories[\"Fuel type\"])\n",
    "color = st.selectbox(\"Color\", categories[\"Color\"])\n",
    "leather_interior = st.selectbox(\"Leather Interior\", categories[\"Leather interior\"])\n",
    "wheel = st.selectbox(\"Wheel\", categories[\"Wheel\"])\n",
    "\n",
    "# ==========================\n",
    "# 3. Encode Inputs\n",
    "# ==========================\n",
    "features_cat = {\n",
    "    \"Manufacturer\": LabelEncoders[\"Manufacturer\"].transform([manufacturer])[0],\n",
    "    \"Model\": LabelEncoders[\"Model\"].transform([model_name])[0],\n",
    "    \"Category\": LabelEncoders[\"Category\"].transform([category])[0],\n",
    "    \"Fuel type\": LabelEncoders[\"Fuel type\"].transform([fuel_type])[0],\n",
    "    \"Color\": LabelEncoders[\"Color\"].transform([color])[0],\n",
    "    \"Leather interior\": LabelEncoders[\"Leather interior\"].transform([leather_interior])[0],\n",
    "    \"Wheel\": LabelEncoders[\"Wheel\"].transform([wheel])[0]\n",
    "}\n",
    "\n",
    "# Final feature array\n",
    "input_data = np.array([[levy, engine_vol, mileage, cylinders, airbags, prod_year,\n",
    "                        features_cat[\"Manufacturer\"], features_cat[\"Model\"],\n",
    "                        features_cat[\"Category\"], features_cat[\"Fuel type\"],\n",
    "                        features_cat[\"Color\"], features_cat[\"Leather interior\"],\n",
    "                        features_cat[\"Wheel\"]]])\n",
    "\n",
    "# ==========================\n",
    "# 4. Predict\n",
    "# ==========================\n",
    "if st.button(\"Predict Price\"):\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\"✅ The estimated price is ${prediction[0]:,.2f}\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
