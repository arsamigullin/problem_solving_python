


if __name__ == '__main__':
    envs = ['inex',
'aenorune',
'swax',
'torayhungarylive',
'dovevivoprod',
'pelicanprd',
'cengiz',
'dsstall',
'ssdemoprod',
'pettibone',
'alipm',
'simmonsbank',
'hometown']

    sb = ['adsntestky6bcyrj',
'cwbuatezbu86cs',
'samuatv6ygwgjp',
'perfsflneyn2od',
'manuatestuntimijh',
'filasandbox1hj8fau8',
'ductoruatkf059r2z',
'alkionteste42zh6fl',
'ssdemosand2ateqere',
'pettiboneuatuvtp2c19',
'msftbb1prjr7kxm',
'Idxsati1k6equ9',
'hometownstage1hqu78djt',
'dfout0u5ps37q',
'dfoqaq8adv2i5']

    for env in sb:
        query = f"SELECT c.LcsEnvironmentId, c.TopologyInstanceName, c.DeploymentItems[0].Customizations[2].SelectedValue, max(c.CreatedAt) FROM c " \
        f"where startswith(c.DeploymentItems[0].Customizations[2].SelectedValue, '{env}') group by c.LcsEnvironmentId, " \
        f"c.TopologyInstanceName, c.DeploymentItems[0].Customizations[2].SelectedValue;"
        query2 = f"SELECT c.LcsEnvironmentId, c.TopologyInstanceName, max(c.CreatedAt) as cd " \
                 f"from c JOIN (SELECT b.SelectedValue as FieldName " \
                 f"from b in c.DeploymentItems[0].Customizations  " \
                 f"where b.FieldName = 'KeyVault' and startswith(b.SelectedValue, '{env}')) k " \
                 f"group by c.LcsEnvironmentId, c.TopologyInstanceName"


        print(query2)