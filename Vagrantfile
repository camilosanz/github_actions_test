# -*- mode: ruby -*-
# vi: set ft=ruby :


N = 1

nodes = [
  {
    :node => "main00",
    :cpu => 4,
    :mem => 8024
  }
]


Vagrant.configure(2) do |config|

  (1..N).each do |node_id|
    nid = (node_id - 1)

    config.env.enable
    config.ssh.insert_key = false
    config.vm.define "main0#{nid}" do |node|
      node.vm.box = "ubuntu/jammy64"
      node.vm.provider "virtualbox" do |vb|
        nodes.each do |custom_node|
          if custom_node[:node] == "main0#{nid}"
            vb.customize ["modifyvm", :id, "--cpus", custom_node[:cpu]]
            vb.customize ["modifyvm", :id, "--memory", custom_node[:mem]]
          end
        end
      end
      node.vm.hostname = "main0#{nid}"
      node.vm.provision :docker
      node.vm.provision :docker_compose
      node.vm.provision "shell" do |s|
        s.path = "./scripts/runner_provision.sh"
        s.args = [
          ENV['RUNNER_URL'],
          ENV['GITHUB_URL'],
          ENV['GITHUB_TOKEN'],
          "runner_#{nid}",
          ENV['RUNNER_DIR'],
          ENV['RUNNER_VERSION'],
          ENV['GITHUB_HASH'],
        ]
        s.privileged = false
      end
    end

  end
end