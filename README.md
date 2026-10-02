# Kind Studio: Run An Engine Job

You'll run a small Epidemic Engine job in your own Kind cluster.
The job counts sample events by region and event type.
Kubernetes supplies both the script and the events as configuration, so you
don't build an image.

You need a running Kind cluster and `kubectl` from C04: Kubernetes Object Map.
No cluster? Pair with a neighbor and write down the step that failed and its
error for the October 5 and 7 discussion sections.

## Steps

1. Check that `kubectl` reaches your cluster:

   ```bash
   kubectl get nodes
   ```

1. Turn the two files into ConfigMaps:

   ```bash
   kubectl create configmap count-script --from-file=count_events.py
   kubectl create configmap engine-events --from-file=events.jsonl
   ```

1. Open `job-template.yaml` and fill in the six `____` blanks.
   The comments say what each blank needs.
1. Apply it:

   ```bash
   kubectl apply -f job-template.yaml
   ```

1. Watch it finish, then read what it printed:

   ```bash
   kubectl get jobs
   kubectl logs job/count-events
   ```

   Done looks like a `Complete` job and a table of counts that ends with
   `total 24`.

## When It Doesn't Work

Run `kubectl describe pod -l job-name=count-events` and read the Events at
the bottom.
A Job can't be edited once it runs, so after a fix:

```bash
kubectl delete job count-events
kubectl apply -f job-template.yaml
```

## Clean Up

```bash
kubectl delete job count-events
kubectl delete configmap count-script engine-events
```
