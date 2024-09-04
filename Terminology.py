#TERMINOLOGY TO KNOW FOR THE PROJECT

"""
Network entities to know and understand:
- AP: Also known as access point ~ Often a wireless connection
- AC: Devices in wireless networks that manage and control access points (APs). They provide centralized
management for configuring APs. Such functions include:
    - Handling network settings
    - Security concerns
    - Handling other parameters
- ACs help manage things from a single location, ensuring control and streamline network management.

- Wifi Roaming: A wireless client device transitions from one AP to another within the same wireless
network without losing connectivity.
- When going from one area to another, a client might experience a situation where their current wi-fi
gets weaker. To combat this, the device will transfer from one network to another seamlessly. It has to
be done seamlessly.

"""
"""
Wifi Roaming has several key processes and technologies that ensure smooth transitions between APs: 
- 802.11k: Radio Resource Management ~ Helps us understand the wireless environment by providing information 
about nearby APs. A client can make more informed decisions on where to roam. Information includes: 
    1) Signal strength 
    2) Channels 
    3) Loads of surrounding APs. 
    
- 802.11v: Network-Assisted Roaming ~ Enables network to assist with roaming decisions. Inform client on 
best AP to connect to based on factors like network load and client location. Includes power-saving 
features to help client manage battery life more effectively during roaming. 

- 802.11r: Fast BSS Transition ~ Reduces the amount of time required to switch from one AP to another by 
streamlining the authentication process. Clients would have to go through a complete reauthentication 
process, causing delays. This transition helps pre-autheticate with new AP while connected to current one. 
Helps with faster hand-offs. 
"""

