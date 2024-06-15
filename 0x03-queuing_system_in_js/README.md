## Queuing system in JS
#### Learning Objectives
<ul>
<li>How to run a Redis server on your machine</li>
<li>How to run simple operations with the Redis client</li>
<li>How to use a Redis client with Node JS for basic operations</li>
<li>How to store hash values in Redis</li>
<li>How to deal with async operations with Redis</li>
<li>How to use Kue as a queue system</li>
<li>How to build a basic Express app interacting with a Redis server</li>
<li>How to the build a basic Express app interacting with a Redis server and queue</li>
</ul>
<p>To Download, extract, and compile the latest stable Redis version use the following commands:
<ul>
<li><code>wget http://download.redis.io/releases/redis-6.0.10.tar.gz</code></li>
<li><code>tar xzf redis-6.0.10.tar.gz</code></li>
<li><code>cd redis-6.0.10</code></li>
<li><code>make</code></li>
</ul>
Start Redis in the background with <code>src/redis-server</code>
Kill the server with the process id of the redis-server (hint: use ps and grep)
<code>kill [PID_OF_Redis_Server]</code>
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.
</p>