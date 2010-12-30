require 'rake/rpm-utils'

task :update_war,:war_name,:release,:release_dir do |t, args|
  war_name = args[:war_name]
  cdir = Dir.pwd
  dir = "abiquo-#{war_name}-#{args[:release]}"
  `scp root@hudson:/opt/releases/#{args[:release_dir]}/premium/#{war_name}.war .`
  Dir.mkdir dir
  Dir.chdir dir
  `unzip ../#{war_name}.war`
  Dir.chdir cdir
  `tar czf #{dir}.tar.gz #{dir}`
  `rm -rf #{dir} #{war_name}.war`
end
