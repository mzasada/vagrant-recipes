vagrant-recipes
===============

Handful of VM setups using [Vagrant](http://www.vagrantup.com/) and [fabric](http://www.fabfile.org/) provisioning. 

Assuming one have [pip](https://pip.pypa.io/en/latest/) installed, all python dependencies might be installed using

`pip install -r requirements.txt`

There is a vagrant plugin needed to run the box. Having Vagrant installed, one may type

`vagrant plugin install vagrant-fabric`

Having vagrant and all python dependencies installed, one can deal with the VM 
using common Vagrant commands, e.g.
`vagrant up`

Special thx to [wutali](https://github.com/wutali/vagrant-fabric) 
and [hanskoff](https://github.com/hanskoff/vagrant-fabric) for inspiration.