# PoC: HTTP/2 CONTINUATION Flood Vulnerability
This is a proof of concept for the HTTP/2 CONTINUATION flood vulnerability published by 
[nowotarski.info](https://nowotarski.info/) on April 03, 2024.  

This vulnerability can lead to different consequences for vulnerable web servers:
- CPU exhaustion
- Out Of Memory crash (After a single or multiple connections)
- Crash after a few frames sent  

(more details in [the blog post of nowotarski](
https://nowotarski.info/http2-continuation-flood-technical-details/))

The vulnerable go server in this PoC leads to CPU exhaustion. 

## Usage
Start the vulnerable go server:
```shell
cd vulnerable-go-server
docker build -t vulnerable-go-server .
docker run -p 8000:8000 vulnerable-go-server -d
```

Install the required prerequisites:
```shell
pip install h2
```

Execute the Proof of Concept:
```shell
python3 poc.py
```

## Affected CVEs
- CVE-2024-27983
- CVE-2024-27919
- CVE-2024-2758
- CVE-2024-2653
- CVE-2023-45288
- CVE-2024-28182
- CVE-2024-27316
- CVE-2024-31309
- CVE-2024-30255

## References
- [HTTP/2 CONTINUATION Flood: Technical Details](https://nowotarski.info/http2-continuation-flood-technical-details/)
- [HTTP/2 CONTINUATION frames can be utilized for DoS attacks](https://kb.cert.org/vuls/id/421644)
