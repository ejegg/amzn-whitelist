# amzn-whitelist
Calculate IP ranges for Amazon MWS servers

Uses wget to fetch the list of [AWS IP address ranges](http://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html)
and [jq](https://stedolan.github.io/jq/) to include only us-east-1 ranges
and exclude everything listed as belonging to a hosted service such as
EC2 or Cloudfront.

Network IP calculations are done in Python using the [netaddr](https://pypi.python.org/pypi/netaddr) library.

GPL v3.0+
