aws_infra_data = {
"compute": {
"total_ec2_instances": 5000,
"running_instances": 4500,
"stopped_instances": 500,
"average_cpu_utilization_percent": 65,
"average_memory_utilization_percent": 70,
"annual_cost_million_usd": 25
},
"storage": {
"s3_buckets": 150,
"total_storage_tb": 20000,
"used_storage_tb": 15000,
"glacier_storage_tb": 5000,
"monthly_storage_cost_million_usd": 3
},
"network": {
"total_vpcs": 50,
"subnets_per_vpc": 10,
"monthly_data_transfer_tb": 1000,
"data_transfer_cost_million_usd": 2,
"average_latency_ms": 25
},
"databases": {
"total_rds_instances": 300,
"active_rds_instances": 250,
"idle_rds_instances": 50,
"monthly_rds_cost_million_usd": 4,
"backup_storage_tb": 500
},
"security": {
"active_security_groups": 1000,
"unused_security_groups": 200,
"monthly_security_cost_million_usd": 1,
"average_threat_detection_per_month": 500
},
"monitoring": {
"cloudwatch_alarms": 1200,
"active_alarms": 300,
"log_storage_tb": 100,
"monthly_monitoring_cost_million_usd": 0.5,
"average_response_time_ms": 200
}
}

