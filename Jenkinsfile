
def webents=[mk-aggregator,mk-smart-webent,mk-wm-msger,mk-app-webent,mk-job-webent,mk-openApi,mk-wm-webent,mk-yum-webent,mk-imgr-webent,mk-uic-webent,mk-qdragon-webent,mk-sn-webent,mk-intf-webent,mk-kunlun-webent,mk-imgr-rpc,mk-yum-rpc,mk-mdata-rpc,mk-uic-rpc,mk-sn-rpc]

stage 'pull code'
node {
       sh "bash ~/ci/pull.sh"
     }
}

stage 'build aggregator'
node {
       sh "bash ~/ci/build.sh 0"
}

stage 'build webents'
buildlist=[:]
for (int i = 1; i < webents.size()-4; i++3){
    buildlist = webents[${i}]: {
         node {
                sh "bash ~/ci/build.sh ${i}"
              }
    }, webents[${i+1}]: {
         node {
                sh "bash ~/ci/build.sh ${i+1}"
              }
         }
    },webents[${i+2}]: {
         node {
                sh "bash ~/ci/build.sh ${i+2}"
              }
    }
    parallel buildlist
}

stage 'deploy'
deloplist=[:]
for (int i = 1; i < webents.size()-4; i++3){
    deloplist = webents[${i}]: {
         node {
                sh "bash ~/ci/deploy.sh ${i}"
              }
    }, webents[${i+1}]: {
         node {
                sh "bash ~/ci/deploy.sh ${i+1}"
              }
         }
    },webents[${i+2}]: {
         node {
                sh "bash ~/ci/deploy.sh ${i+2}"
              }
    }
    parallel deloplist
}

