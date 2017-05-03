node 'mk' {
def webents=[mk-aggregator,mk-smart-webent,mk-wm-msger,mk-app-webent,mk-job-webent,mk-openApi,mk-wm-webent,mk-yum-webent,mk-imgr-webent,mk-uic-webent,mk-qdragon-webent,mk-sn-webent,mk-intf-webent,mk-kunlun-webent,mk-imgr-rpc,mk-yum-rpc,mk-mdata-rpc,mk-uic-rpc,mk-sn-rpc]

stage 'pull code'
steps {
       sh "bash ~/ci/pull.sh"
     }

stage 'build aggregator'
steps {
       sh "bash ~/ci/build.sh 0"
}

stage 'build webents'
def buildlist=[:]
for (int i = 1; i < webents.size()-4; i=i+3){
    buildlist[webents[${i}]]= {
         steps {
                sh "bash ~/ci/build.sh ${i}"
              }
    }
    buildlist[webents[${i+1}]]= {
         steps {
                sh "bash ~/ci/build.sh ${i+1}"
              }
    }
    buildlist[webents[${i+2}]]= {
         steps {
                sh "bash ~/ci/build.sh ${i+2}"
              }
    }
    parallel buildlist
}

stage 'deploy'
def delopylist=[:]
for (int i = 1; i < webents.size()-4; i=i+3){
    delopylist[webents[${i}]]={
         steps {
                sh "bash ~/ci/deploy.sh ${i}"
              }
    }
    delopylist[webents[${i+1}]]={
         steps {
                sh "bash ~/ci/deploy.sh ${i+1}"
              }
    }
    delopylist[webents[${i+2}]]= {
         steps {
                sh "bash ~/ci/deploy.sh ${i+2}"
              }
    }
    parallel deloplist
}

}