Smart Public Transit with Geofencing, Predictive Analytics, and Sustainability - BramHacks 2024
Introducing our first hackathon project at BramHacks 2024, where our team developed an innovative model to optimize public transit in Brampton using Geofencing, Real-Time Passenger Tracking , Machine Learning (ML), and Sustainability Initiatives. This solution aims to improve efficiency, reduce congestion, and promote sustainable transportation.
Key Features and Innovations:
1. Geofencing and Real-Time Passenger Tracking 
The model we developed uses Geofencing to create virtual boundaries around bus stops, defined by 50-100 meter radii based on GPS coordinates. RFID scanners are installed at bus stops, which track the number of passengers waiting as well as the number of passengers deboarding the bus. When passengers scan their PRESTO card upon exiting, the RFID scanners send real-time data to the Command Center, giving operators visibility into foot traffic at each bus stop.
This data helps in predicting peak times and adjusting bus schedules in real time, improving overall operational efficiency. It also prevents overcrowding by ensuring buses arrive when there is sufficient demand.
2. AI-Powered Footfall Predictions
To forecast passenger flow and improve scheduling, we used Python to train our Machine Learning model on real-time data from Brampton Transit. This data includes information on bus occupancy, passenger boarding patterns, and trip frequency across different routes. By feeding this data into our Random Forest model, we were able to predict the number of passengers likely to deboard at each bus stop, as well as forecast footfall throughout the day.
This allows for:
- Predicting peak times and adjusting service accordingly.
- Planning for Ad-Hoc buses during high-demand hours.
- Ensuring buses are deployed efficiently and on time.
3. Real-Time Data Integration with Brampton Transit 
Our model integrates with real-time data from Brampton Transit, which includes:
- Total occupancy in vehicles.
- Passenger boarding counts for the top 5 routes.
- Frequency of bus trips on each route.
While Brampton Transit tracks whether a bus is full and the total number of passengers boarding, our model enhances this data by predicting deboarding patterns at specific stops and offering a clearer view of passenger flow. This enables better decision-making for bus operators and improves passenger experience by minimizing overcrowding.

4.RFID-Based Real-Time Tracking at Bus Stops 
In addition to the integration with Brampton Transit, our hardware solution involves the use of an RFID scanner built during the hackathon. We constructed a photosensor device using an MPU (Microcontroller Processing Unit), which acts as a counter at bus stops. This device tracks the number of passengers deboarding as well as the number of people waiting at each stop, sending this data to the Command Center for real-time monitoring.
By scanning the PRESTO cards of passengers as they deboard, the RFID scanner sends the count to the Command Center, providing operators with critical information on passenger flow at each stop. This allows for better management of bus schedules and optimizes the frequency of buses based on real-time demand. 
This hardware innovation helps to improve the accuracy of data collection at bus stops, enabling operators to make more informed decisions.
5. Loyalty Program and Rewards  
To encourage more people to use public transit, we integrated a Loyalty Program with PRESTO cards. Passengers earn points every time they use Brampton Transit, and these points can be redeemed for rewards like free trips, monthly passes, and other benefits. This incentivizes sustainable travel and promotes the use of public transit, helping to reduce congestion.
6. Promoting Sustainability with Cycle-Leasing Programs
As part of our sustainability initiative, we’ve introduced a Cycle Leasing Program, allowing passengers to rent bikes for a small fee. This supports the Bike and Ride program in Brampton, promoting healthier commuting options and reducing carbon emissions. Passengers can combine cycling with transit, contributing to a more eco-friendly transportation system.
7. Bravo: Brampton Advanced Vehicle Operation App
We also worked on the development of a prototype app called Bravo, which provides passengers with the following features:
- Real-time bus tracking, showing nearby bus stops and arrival times.
- Earn loyalty points for using public transit and scan PRESTO cards for access to rewards.
- Footfall data display, showing how crowded a bus stop is in real time.
- Issue reporting: Passengers can report issues such as buses being full or late, which are sent directly to the Command Center for resolution.
Main Features of the App:
- Transit Time Monitoring: View current bus schedules and check if a bus stop is busy based on real-time data.
-Footfall Information: See how many people are waiting at bus stops, helping users avoid crowded areas.
- Reporting System: Passengers can report issues, helping the **Command Center** improve operations.
8. Budget-Conscious, Scalable, and Resource-Efficient Solution  
Our solution is designed to be cost-effective , scalable, and resource-efficient. By using Geofencing, Machine Learning, real-time data, and hardware innovation  like the photosensor device or RFID scanner, we optimize bus schedules and operations to ensure that resources are used effectively. This approach helps to reduce waste, lower energy consumption, and minimize environmental impact.
This model addresses key challenges facing Brampton Transit, including overcrowding, inefficient bus schedules, and the lack of real-time data for operational decision-making. By integrating Geofencing, RFID-based tracking, AI-powered predictions, and sustainability programs, our solution helps improve service reliability, encourages the use of public transit, and supports a more sustainable and efficient transportation system.
