from airflow_client.sdk.dag import DAG
# 实例任务




dag = DAG('192.168.200.40','8090','admin','12345678', # Airflow服务连接信息
          {                                           # 任务描述结构
            'info':{'owner':'abc'},                   # 建议与租户标识保持一致（涉及运行日志查看权限）
            'edges':[{"source_id": "dummy1", "target_id": "select2"}], # 多个任务间的依赖关系
            'tasks':{                                                  # 每个任务的具体描述
                "dummy1":                                              # 任务ID
                    {"task_type": "DummyOperator"}, 
                "select2": {"task_type": "SqlOperator",                # 任务类型
                            "params":{"sql_conn_id": "gp-192.168.0.178", "sql_type": "postgres", "sql": "select 2"}} # 任务参数
                }
          })


# 运行任务
status = dag.run(conf={}, timeout=10)
print(str(status.get('state')))
