# Bug-Hunting
> Get All Hidden Urls from JS file
```
cat urls.txt | grep -i "\.js$" | while read url do; do echo " [$] $url" ;echo "$url" | curl -s $url | ./extract.rb ; echo "\n\n\n" ;done | tee js.txt
```
> Find Subdomain using crt.sh
```
python3 crt.py -d "domain.com"
```
