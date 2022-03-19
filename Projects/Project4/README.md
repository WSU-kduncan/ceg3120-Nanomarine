1. I created a [config](https://github.com/WSU-kduncan/ceg3120-Nanomarine/blob/main/Projects/Project4/ssh%20config.PNG) file in each instance that contains the hostnames of the other two instances.
2. Once you ssh into the "proxy" instance, all you have to do is input "ssh web1/web2/proxy" depending on where you wish to go.
3. I modified the "haproxy.cfg" file in /etc/haproxy. I just added a frontend and backend to the file that contained the information on both web servers. After modifying the files, I ran "sudo systemctl restart haproxy" to restart the service. I followed the lecture to complete this part.
4. I modified the index file located at "/var/www/html" in both server instances. This was the file that the default page for apache told me to modify, so I did.
5. [server1](https://github.com/WSU-kduncan/ceg3120-Nanomarine/blob/main/Projects/Project4/server1.PNG), [server2](https://github.com/WSU-kduncan/ceg3120-Nanomarine/blob/main/Projects/Project4/server2.PNG) 
