name=$(cat *.spec | grep -i Name: | awk '{print $NF}')
#repo_url=$(cat *.spec | grep -i URL: | awk '{print $NF}')
git clone --depth 1 https://github.com/LadybirdBrowser/ladybird.git $name
cd $name
git archive --format=tar --prefix $name-$(date +%Y%m%d)/ HEAD | zstd --ultra -22 > ../$name-$(date +%Y%m%d).tar.zst
cd -
