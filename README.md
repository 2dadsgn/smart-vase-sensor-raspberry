# Smart Vase
No more hussle checking your plant's hydration or the right sunlight exposure, with this python app you can easily monitor your plants.
The app gathers data about light exposure and soil's humidity and send it to a web-app based on the raspberry pi itself.

<h3>List of file explained</h3>

--- DHT11.py---

Used for the data readings through the DHT11 for humidty and temperature.


---mongoconn.py---

External function to insert data into the Database.

---raspsocket.py---

External function to deliver data to the web-app server

--- smart-vase.py---
The main function with an ethernal loop to monitor the plant  and pack the data up to send it to the server.

